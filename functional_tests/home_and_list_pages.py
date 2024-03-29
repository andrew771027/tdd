from selenium.webdriver.common.by import By

ITEM_INPUT_ID = 'id_text'


class HomePage(object):

    def __init__(self, test):
        self.test = test

    def go_to_home_page(self):
        self.test.browser.get(self.test.server_url)
        self.test.wait_for(self.get_item_input)
        return self

    def go_to_my_lists_page(self):
        self.test.browser.find_element(By.LINK_TEXT, 'My lists').click()
        self.test.wait_for(lambda: self.test.assertEqual(
            self.test.browser.find_element(By.TAG_NAME, 'h1').text, 'My List'))
        return self

    def get_item_input(self):
        return self.test.browser.find_element(By.ID, ITEM_INPUT_ID)

    def start_new_list(self, item_text):
        self.go_to_home_page()
        input_box = self.get_item_input()
        input_box.send_keys(item_text + '\n')
        list_page = ListPage(self.test)
        list_page.wait_for_new_item_in_list(item_text, 1)
        return list_page


class ListPage(object):

    def __init__(self, test):
        self.test = test

    def get_list_table_rows(self):
        return self.test.browser.find_element(By.CSS_SELECTOR, '#id_list_table tr')

    def wait_for_new_item_in_list(self, item_text, position):
        expected_row = f'{position}: {item_text}'
        self.test.wait_for(lambda: self.test.assertIn(
            expected_row, [row.text for row in self.get_list_table_rows()]))

    def get_share_box(self):
        return self.test.browser.find_element(By.CSS_SELECTOR, 'input[name=email]')

    def get_shared_with_list(self):
        return self.test.browser.find_element(By.CSS_SELECTOR, '.list-sharee')

    def get_item_input(self):
        return self.test.browser.find_element(By.ID, ITEM_INPUT_ID)

    def add_new_item(self, item_text):
        current_pos = len(self.get_list_table_rows())
        self.get_item_input().send_keys(item_text + '\n')
        self.wait_for_new_item_in_list(item_text, current_pos + 1)

    def share_list_with(self, email):
        self.get_share_box().send_keys(email + '\n')
        self.test.wait_for(
            lambda: self.test.assertIn(
                email, [item.text for item in self.get_shared_with_list()])
        )
