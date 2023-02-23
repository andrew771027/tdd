from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_retrieve_it_later(self):

        self.browser.get("http://localhost:8000")

        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn("To-Do", header_text)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute(
            'placeholder'), "Enter a to-do item")

        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == "1. Buy peacock features' for row in rows" for row in rows),
            "New to-do item did bot appear in table"
        )

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
