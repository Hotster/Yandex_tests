import pytest
from pages.search_page import SearchPage
from pages.images_main_page import ImagesMainPage
from pages.images_result_page import ImagesResultPage


@pytest.mark.usefixtures('driver')
class TestYandexImages:
    URL = "https://yandex.ru"

    def test_images(self, driver):
        search_page = SearchPage(driver)
        images_main_page = ImagesMainPage(driver)
        images_result_page = ImagesResultPage(driver)

        # Go to https://yandex.ru
        search_page.go_to_yandex(self.URL)
        # Check if the 'Images' link is on the page.
        search_page.images_link_displayed()
        # Click on the 'Images' link.
        search_page.images_click()
        # Check if the link matches current URL.
        images_main_page.images_url()
        # Click on the 'Category' link.
        category_text = images_main_page.open_category()
        # Check if the category name matches the opened page.
        images_result_page.category_text_check(category_text)
        # Open and save an image.
        image_1 = images_result_page.open_image()
        # Click on the 'Next' button.
        images_result_page.next_image()
        # Click on the 'Previous' button and save the image.
        image_2 = images_result_page.prev_image()
        # Compare two images.
        images_result_page.compare_images(image_1, image_2)
