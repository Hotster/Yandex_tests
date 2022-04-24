import pytest
from pages.search_page import SearchPage
from pages.results_page import ResultPage


@pytest.mark.usefixtures('driver')
class TestYandexSearch:
    def test_search_yandex(self, driver):
        search_page = SearchPage(driver)
        search_page.search_field_displayed()

    def test_suggest_field(self, driver):
        search_page = SearchPage(driver)
        search_page.search('Тензор')
        search_page.displayed_field_existence()

    def test_enter_field(self, driver):
        search_page = SearchPage(driver)
        search_page.search('Тензор')
        search_page.press_enter()

    def test_site_in_5_results(self, driver):
        search_page = SearchPage(driver)
        result_page = ResultPage(driver)
        search_page.search('Тензор')
        search_page.press_enter()
        assert result_page.displayed_in_5_results() is True, 'Link is not in results'
