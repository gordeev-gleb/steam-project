from containers.auth_page import LoginPage
from utils.utils import BaseActions as BaseA


class AuthFlows:
    @staticmethod
    def enter_account_name(browser, value):
        BaseA.find_element(browser, LoginPage.name_field()).send_keys(value)

    @staticmethod
    def enter_password(browser, value):
        BaseA.find_element(browser, LoginPage.pass_field()).send_keys(value)

    @staticmethod
    def click_login_btn(browser):
        BaseA.find_element(browser, LoginPage.login_btn()).click()
