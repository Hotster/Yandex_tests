import pytest
from pathlib import Path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome


@pytest.fixture(scope='session')
def driver():
    driver_dir = str(Path(__file__).parent.parent.joinpath('drivers\\chromedriver'))
    driver = Chrome(service=Service(driver_dir))
    yield driver
    driver.quit()
