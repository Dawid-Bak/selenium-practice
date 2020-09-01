import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from tests.page_objects.home_page_object import HomePage
from tests.page_objects.search_page_object import SearchPage


@pytest.fixture(scope='session')
def headless():
	options = webdriver.ChromeOptions()
	options.add_argument("--headless")
	options.add_argument("--window-size=1920,1080")
	return options


@pytest.fixture(scope='session')
def browser(headless):
	driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=headless)
	yield driver
	driver.quit()


@pytest.fixture(scope='class')
def home_page(browser):
	return HomePage(browser)


@pytest.fixture(scope='class')
def search_page(browser):
	return SearchPage(browser)
