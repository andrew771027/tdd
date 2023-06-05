from .base import FunctionalTest
from unittest import skip
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element(By.CSS_SELECTOR, '.has-error')

    def test_cannot_add_empty_list_items(self):

        # Edith 前往首頁，並不小心試著提交
        # 一個空的清單項目。他在空的輸入方塊中按下Enter
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)
        
        # 首頁重新整理，有一個錯誤訊息
        # 說不能有空的清單選項
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item.")

        # 他再試一次，在項目中加入一些文字，現在可以動作了
        self.get_item_input_box().send_keys('Buy milk')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')

        # 離譜的是，現在他決定要提交地按個空白的清單項目
        self.get_item_input_box().send_keys(Keys.ENTER)

        # 他在清單網頁上看到類似的警告
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item.")

        # 她可以填入一些文字來修正它
        self.get_item_input_box().send_keys('Make tea')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
    
    def test_cannot_add_duplicate_items(self):

        # Edith 前往首頁，開始編輯一個新的清單
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy wellies')

        # 他不小心試著輸入一個重複的項目
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)

        # 他看到一個有用的錯誤訓息
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list.")
    
    def test_error_messages_are_cleared_on_input(self):

        # Edith 在開始新的一個串列時，會產生驗證錯誤:
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # 他開始在輸入放塊中打字，以清除錯誤
        self.get_item_input_box().send_keys('a')

        # 他開心地看到錯誤訊息不見了
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())