from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

# CSS Selectors
search_icon = '.noo-search'


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def click_on_element(self, selector):
        element = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        element.click()

    def click_search_button(self):
        self.click_on_element(search_icon)

    def wait_for_element_visible(self, selector):
        return self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_for_elements_visible(self, selector):
        return self.wait.until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, selector)))

    def get_element_height(self, selector):
        element = self.wait_for_element_visible(selector)
        return element.size['height']

    def scroll_to_element(self, selector):
        element = self.wait_for_element_visible(selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def fix_scroll_position(self, selector):
        height = self.get_element_height(selector)
        self.driver.execute_script("window.scrollBy(0, arguments[0]);", -height)
