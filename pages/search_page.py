from pages.base_page import BasePage
from resources.locators import SearchPageLocators


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_yandex(self, url):
        self.driver.get(url)

    def search(self, text):
        self.enter_text(SearchPageLocators.search_field, text)

    def press_enter(self):
        self.press_enter_button(SearchPageLocators.search_field)

    def search_field_displayed(self):
        return self.is_displayed(SearchPageLocators.search_field)

    def suggest_field_displayed(self):
        return self.is_displayed(SearchPageLocators.suggest_field)

    def images_link_displayed(self):
        return self.is_displayed(SearchPageLocators.images_link)

    def images_click(self):
        self.click(SearchPageLocators.images_link)
        images_window = self.driver.window_handles[1]
        self.driver.switch_to.window(images_window)
