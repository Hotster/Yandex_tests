from pages.base_page import BasePage
from resources.locators import ImagesMainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ImagesMainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def images_url(self):
        url = "https://yandex.ru/images/"
        self.url_check(url)

    def open_category(self):
        category_text = WebDriverWait(self.driver, 10).\
            until(ec.visibility_of_element_located(ImagesMainPageLocators.category)).text
        self.click(ImagesMainPageLocators.category)
        return category_text
