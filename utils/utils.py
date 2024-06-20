from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

TIME_WAIT = 10


class BaseActions:
    @staticmethod
    def find_element(browser, locator):
        return WebDriverWait(browser, TIME_WAIT).until(EC.presence_of_element_located((By.XPATH, locator)))


class JSON:
    @staticmethod
    def credentials(cred):
        with open('credentials.json', 'r') as json_file:
            credentials = json.load(json_file)
        return credentials[cred]
