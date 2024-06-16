from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseActions:
    @staticmethod
    def find_element(browser, locator):
        return WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, locator)))
