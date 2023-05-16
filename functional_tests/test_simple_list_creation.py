from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_retrieve_it_later(self):

        self.browser.get(self.live_server_url)

        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn("To-Do", header_text)

        input_box = self.get_item_input_box()
        self.assertEqual(input_box.get_attribute(
            'placeholder'), "Enter a to-do item")

        self.get_item_input_box().send_keys('Buy peacock feathers')
        self.get_item_input_box().send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        self.check_for_row_in_list_table("1: Buy peacock feathers")
        self.get_item_input_box().send_keys('Use peacock feathers to make a fly')
        self.get_item_input_box().send_keys(Keys.ENTER)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')

        self.check_for_row_in_list_table("1: Buy peacock feathers")
        self.check_for_row_in_list_table(
            "2: Use peacock feathers to make a fly")

        # 新的User造訪
        self.browser.quit()
        self.browser = webdriver.Chrome()
        self.browser.get(self.live_server_url)

        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        self.get_item_input_box().send_keys('Buy milk')
        self.get_item_input_box().send_keys(Keys.ENTER)

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
