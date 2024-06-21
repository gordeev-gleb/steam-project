from selenium.webdriver.common.by import By
from utils.utils import WaitUtils


class LoginPage:
    PIVOT_FORM_LOC = '//*[@data-featuretarget="login"]'
    NAME_FIELD_LOC = (By.XPATH, f'{PIVOT_FORM_LOC}//input[@type="text"]')
    PASS_FIELD_LOC = (By.XPATH, f'{PIVOT_FORM_LOC}//input[@type="password"]')
    LOGIN_BTN_LOC = (By.XPATH, f'{PIVOT_FORM_LOC}//button[@type="submit"]')
    ERROR_MSG_LOC = (By.XPATH, f'{PIVOT_FORM_LOC}//form/div[5]')

    def __init__(self, browser):
        self.browser = browser

    def enter_account_name(self, name):
        WaitUtils.wait_presence_of_element(self.browser, self.NAME_FIELD_LOC).send_keys(name)

    def enter_password(self, password):
        WaitUtils.wait_presence_of_element(self.browser, self.PASS_FIELD_LOC).send_keys(password)

    def click_login_btn(self):
        WaitUtils.wait_presence_of_element(self.browser, self.LOGIN_BTN_LOC).click()

    def login(self, name, password):
        WaitUtils.wait_presence_of_element(self.browser, self.NAME_FIELD_LOC).send_keys(name)
        WaitUtils.wait_presence_of_element(self.browser, self.PASS_FIELD_LOC).send_keys(password)
        WaitUtils.wait_presence_of_element(self.browser, self.LOGIN_BTN_LOC).click()
