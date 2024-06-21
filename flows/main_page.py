from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils


class MainPage:
    PIVOT_FORM_LOC = '//*[@id="global_header"]'
    LOGIN_BUTTON_LOC = (By.XPATH, f'{PIVOT_FORM_LOC}//*[@id="global_action_menu"]/a[2]')

    def __init__(self, browser):
        self.browser = browser

    def click_to_login_button(self):
        WaitUtils.wait_presence_of_element(self.browser, self.LOGIN_BUTTON_LOC).click()
