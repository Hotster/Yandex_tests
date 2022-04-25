from pages.base_page import BasePage
from resources.locators import SearchPageLocators
from resources.locators import ResultPageLocators


class ResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def displayed_in_5_results(self):
        return self.displayed_in_results(SearchPageLocators.search_result, ResultPageLocators.expected_link, 5)
