import pytest
from pages.search_page import SearchPage
from pages.results_page import ResultPage


@pytest.mark.usefixtures('driver')
class TestYandexSearch:
    URL = "https://yandex.ru"

    def test_search_field(self, driver):
        search_page = SearchPage(driver)
        result_page = ResultPage(driver)

        # Go to 'https://yandex.ru'.
        search_page.go_to_yandex(self.URL)
        # Check if the search field is on the page.
        search_page.search_field_displayed()
        # Fill the search field with a content.
        search_page.search('Тензор')
        # Check if the suggestion field is on the page.
        search_page.suggest_field_displayed()
        # Press 'Enter' key.
        search_page.press_enter()
        # Check if results contain required links.
        result_page.displayed_in_5_results()
