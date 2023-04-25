from .base import FunctionalTest
from selenium.webdriver.common.by import By


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)

        self.browser.set_window_size(1027, 768)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2,
                               512,
                               delta=5)

