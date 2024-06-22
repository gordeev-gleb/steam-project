from utils.singleton_driver import WebDriverSingleton
from config import LINK
import pytest


@pytest.fixture(scope="module")
def browser(request):
    language = request.param
    driver = WebDriverSingleton().get_driver(language)
    driver.get(LINK)
    yield driver
    WebDriverSingleton().quit_driver()
