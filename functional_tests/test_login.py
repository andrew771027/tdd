from .base import FunctionalTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import time


class LoginTest(FunctionalTest):

    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail('could not find window')

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: b.find_element(By.ID, element_id))

    def test_login_persona(self):
        # Edith前往行笨的超集清單網站
        # 並且在第一次來到時，發現一個"Sign In"連結
        self.browser.get(self.server_url)
        self.browser.find_element(By.ID, 'id_login').click()

        # 一個Persona登入方塊出現了
        self.switch_to_new_window('Mozilla Persona')
        # Edith用他的Email地址登入
        # 使用mockmyid.com來測試email
        self.browser.find_element(
            By.ID, 'authentication_email').send_keys('edith@mockmyid.com')
        self.browser.find_element(By.TAG_NAME, 'button').click()

        # Persona 視窗關閉
        self.switch_to_new_window('To-Do')

        # 他可以看到他登入
        self.wait_for_element_with_id('id_logout')
        navbar = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertIn('edith@mockmyid.com', navbar.text)
