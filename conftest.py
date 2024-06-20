from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import DRIVER_PATH, LINK
import pytest


@pytest.fixture
def browser():
    service = Service(executable_path=DRIVER_PATH)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(LINK)
    yield driver
    driver.quit()
