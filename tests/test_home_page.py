from tests.config import base_url

expected_header_text = 'FASHION NEWS'


def test_verify_main_url(home_page):
	home_page.navigate_to_home()
	assert home_page.get_url() == base_url


def test_verify_header_text_exist(home_page):
	home_page.navigate_to_home()
	home_page.scroll_to_header_and_fix_position()
	assert home_page.header_text() == expected_header_text
