from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils
from flows.base_page import BasePage


class MainPage(BasePage):
    PIVOT_FORM_LOC = '//*[@id="global_header"]'
    LOGIN_BUTTON_LOC = (By.XPATH, f'{PIVOT_FORM_LOC}//*[@id="global_action_menu"]/a[2]')

    def click_to_login_button(self):
        WaitUtils.wait_presence_of_element(self.browser, self.LOGIN_BUTTON_LOC).click()
