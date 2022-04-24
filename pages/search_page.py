from pages.base_page import BasePage
from resources.locators import SearchPageLocators


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.URL)

    def search(self, text):
        self.enter_text(SearchPageLocators.search_field, text)

    def press_enter(self):
        self.press_enter_button(SearchPageLocators.search_field)

    def search_field_displayed(self):
        return self.is_displayed(SearchPageLocators.search_field)

    def displayed_field_existence(self):
        return self.is_displayed(SearchPageLocators.suggest_field)
