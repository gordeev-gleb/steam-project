import pytest
from selenium import webdriver
from utils.utils import JSON
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="module")
def browser():
    service = Service(executable_path=JSON.credentials('DRIVER_PATH'))
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
