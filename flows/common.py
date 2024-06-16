from containers.common import Header
from selenium.webdriver.common.by import By


class HeaderFlows:
    @staticmethod
    def click_to_login_button(browser):
        return browser.find_element(By.XPATH, Header.login_button(Header())).click()
