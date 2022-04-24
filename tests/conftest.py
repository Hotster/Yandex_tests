import pytest
from pathlib import Path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
import time   # Should delete


@pytest.fixture(scope='function')
def driver():
    driver_dir = str(Path(__file__).parent.parent.joinpath('drivers\\chromedriver'))
    driver = Chrome(service=Service(driver_dir))
    yield driver
    time.sleep(3)   # Should delete
    driver.quit()
