from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from tests.page_objects.base_page import BasePage

# CSS Selectors
search_note_field = 'label.note-search'
search_box = '.form-control'
selector_search_result = '.noo-product-inner'
selector_no_product_found = '.woocommerce-info'
selector_image = '.owl-item.active>a>img'
selector_price = '.price>.woocommerce-Price-amount'
selector_title = '.noo-product-inner>h3'
selector_dots = '.noo-product-item.one>.noo-product-inner>.noo-loop-cart>a'


class SearchPage(BasePage):
    def __init__(self, webdriver):
        self.driver = webdriver
        self.wait = WebDriverWait(self.driver, 10)

    def search_note(self):
        search_note = self.wait_for_element_visible(search_note_field)
        return search_note.text

    def search_for_product(self, product):
        search_field = self.wait_for_element_visible(search_box)
        search_field.click()
        search_field.send_keys(product)
        search_field.send_keys(Keys.RETURN)

    def get_search_results(self):
        return self.wait_for_elements_visible(selector_search_result)

    def get_dots_elements(self, search_results):
        action = ActionChains(self.driver)
        list_dots_element = []
        for element in search_results:
            action.move_to_element(element)
            list_dots_element.append(self.driver.find_element(By.CSS_SELECTOR, selector_dots))
        action.perform()
        return list_dots_element

    def verify_search_results_for_query(self, search_query):
        search_results = self.get_search_results()
        self.verify_search_query_in_search_results(search_query, search_results)
        self.verify_image_exist_in_every_search_result(search_results)
        self.verify_price_in_every_search_result(search_results)
        self.verify_title_in_every_search_result(search_results)
        self.verify_dots_in_every_search_result(search_results)

    def verify_search_results_not_exist(self):
        string_no_product_found = self.wait_for_element_visible(selector_no_product_found)
        assert string_no_product_found.text == 'No products were found matching your selection.'

    def verify_image_exist_in_every_search_result(self, search_results):
        assert len(self.wait_for_elements_visible(selector_image)) == len(search_results)

    def verify_price_in_every_search_result(self, search_results):
        assert len(self.wait_for_elements_visible(selector_price)) == len(search_results)

    def verify_title_in_every_search_result(self, search_results):
        assert len(self.wait_for_elements_visible(selector_title)) == len(search_results)

    def verify_dots_in_every_search_result(self, search_results):
        dots_amount = len(self.get_dots_elements(search_results))
        assert dots_amount == len(search_results)

    @staticmethod
    def verify_search_query_in_search_results(search_query, search_results):
        results_list = []
        for product in search_results:
            results_list.append(product.text.split())
        for product in results_list:
            assert search_query.lower() in [l.lower() for l in product]
