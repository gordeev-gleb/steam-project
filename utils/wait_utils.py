from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TIME_WAIT


class WaitUtils:
    @staticmethod
    def wait_presence_of_element(browser, locator):
        return WebDriverWait(browser, TIME_WAIT).until(EC.presence_of_element_located(locator))
