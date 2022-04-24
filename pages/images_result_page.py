from pages.base_page import BasePage
from resources.locators import ImagesResultPageLocators


class ImagesResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def category_text_check(self, category_text):
        self.driver.find_element(*ImagesResultPageLocators.text)

