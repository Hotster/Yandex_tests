from pages.base_page import BasePage
from resources.locators import ImagesResultPageLocators
from selenium.webdriver.remote.webelement import WebElement

class ImagesResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Not finished
    def category_text_check(self, category_text):
        assert category_text == self.get_item(ImagesResultPageLocators.input_field).get_attribute('value'),\
            "The category text doesn't match the input field value."

    def open_image(self):
        self.click(ImagesResultPageLocators.image)
        return self.get_item(ImagesResultPageLocators.main_image).get_attribute('src')

    def next_image(self):
        self.click_on_invisible(ImagesResultPageLocators.next_button)

    def prev_image(self):
        self.click(ImagesResultPageLocators.back_button)
        return self.get_item(ImagesResultPageLocators.main_image).get_attribute('src')

    @staticmethod
    def compare_images(image_1, image_2):
        assert image_1 == image_2, 'Images are not the same'
