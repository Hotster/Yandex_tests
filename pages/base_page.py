from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(by_locator)).click()

    def press_enter_button(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def is_displayed(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        except TimeoutException:
            raise NoSuchElementException('No such element on page.')

    def displayed_in_results(self, by_locator, by_locator2, results_amount=None):
        links = []
        results = WebDriverWait(self.driver, 10).until(ec.visibility_of_all_elements_located(by_locator))
        if results_amount is None or results_amount > len(results):
            results_amount = len(results)
        for result in range(results_amount):
            try:
                link = results[result].find_element(*by_locator2)
                if link is not None:
                    links.append(link.get_attribute('href'))
            except Exception:
                pass
        assert len(links) > 0, 'No such element on page.'

    def url_check(self, url):
        assert url in self.driver.current_url, f"Link doesn't match the expected link."
