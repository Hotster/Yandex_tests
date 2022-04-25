import pytest

from pages.search_page import SearchPage
from pages.images_main_page import ImagesMainPage
from pages.images_result_page import ImagesResultPage
from resources.locators import ImagesResultPageLocators


@pytest.mark.usefixtures('driver')
class TestYandexImages:
    URL = "https://yandex.ru"

    def test_images(self, driver):
        search_page = SearchPage(driver)
        images_main_page = ImagesMainPage(driver)
        images_result_page = ImagesResultPage(driver)
        search_page.go_to_yandex(self.URL)
        search_page.images_link_displayed()
        search_page.images_click()
        images_main_page.images_url()
        category_text = images_main_page.open_category()
        images_result_page.category_text_check(category_text)
        image_1 = images_result_page.open_image()
        images_result_page.next_image()
        image_2 = images_result_page.prev_image()
        images_result_page.compare_images(image_1, image_2)
