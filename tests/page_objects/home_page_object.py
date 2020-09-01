from selenium.webdriver.support.ui import WebDriverWait
from tests.config import base_url
from tests.page_objects.base_page import BasePage

# CSS Selectors
selector_header = '.noo-shblog-header>h3'
selector_navbar = '.noo-header'


class HomePage(BasePage):
    def __init__(self, webdriver):
        self.driver = webdriver
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to_home(self):
        self.navigate_to(base_url)

    def scroll_to_header_and_fix_position(self):
        self.scroll_to_element(selector_header)
        self.fix_scroll_position(selector_navbar)

    def header_text(self):
        header_text = self.wait_for_element_visible(selector_header)
        return header_text.text
