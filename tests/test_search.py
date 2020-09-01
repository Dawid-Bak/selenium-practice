search_item_dress = 'dress'
expected_search_note = 'TYPE AND PRESS ENTER TO SEARCH'


def test_search_note_is_displayed(home_page, search_page):
    home_page.navigate_to_home()
    home_page.click_search_button()
    assert search_page.search_note() == expected_search_note


def test_search_results(home_page, search_page):
    home_page.navigate_to_home()
    home_page.click_search_button()
    search_page.search_for_product(search_item_dress)
    search_page.verify_search_results_for_query(search_item_dress)


def test_empty_search_results(home_page, search_page):
    home_page.navigate_to_home()
    home_page.click_search_button()
    search_page.search_for_product('not existing product')
    search_page.verify_search_results_not_exist()
