from utils.utils import BaseActions as BaseA


class LoginPage:
    pivot_xpath = '//*[@data-featuretarget="login"]'
    name_field = f'{pivot_xpath}//input[@type="text"]'
    pass_field = f'{pivot_xpath}//input[@type="password"]'
    login_btn = f'{pivot_xpath}//button[@type="submit"]'
    error_msg = f'{pivot_xpath}//form/div[string-length(text()) >15]'

    @staticmethod
    def enter_account_name(browser, value):
        BaseA.find_element(browser, LoginPage.name_field).send_keys(value)

    @staticmethod
    def enter_password(browser, value):
        BaseA.find_element(browser, LoginPage.pass_field).send_keys(value)

    @staticmethod
    def click_login_btn(browser):
        BaseA.find_element(browser, LoginPage.login_btn).click()
