from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TIME_WAIT
import json


class WaitUtils:
    @staticmethod
    def wait_presence_of_element(browser, locator):
        return WebDriverWait(browser, TIME_WAIT).until(EC.presence_of_element_located(locator))


class JSON:
    with open('test_data.json', 'r') as json_file:
        credentials = json.load(json_file)

    @staticmethod
    def get_credentials(cred):
        return JSON.credentials[cred]
