import pytest
from pages.search_page import SearchPage
from pages.results_page import ResultPage


@pytest.mark.usefixtures('driver')
class TestYandexSearch:
    URL = "https://yandex.ru"

    def test_search_field(self, driver):
        search_page = SearchPage(driver)
        result_page = ResultPage(driver)
        search_page.go_to_yandex(self.URL)
        search_page.search_field_displayed()
        search_page.search('Тензор')
        search_page.suggest_field_displayed()
        search_page.press_enter()
        result_page.displayed_in_5_results()
