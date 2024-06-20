from flows.common import Header
from flows.auth_page import LoginPage
from utils.utils import BaseActions as BaseA, JSON


def test_google_search(browser):
    browser.get(JSON.credentials('LINK'))
    Header.click_to_login_button(browser)
    LoginPage.enter_account_name(browser, JSON.credentials('STEAM_LOGIN'))
    LoginPage.enter_password(browser, JSON.credentials('STEAM_PASSWORD'))
    LoginPage.click_login_btn(browser)
    assert BaseA.find_element(browser, LoginPage.error_msg).text == \
           'Please check your password and account name and try again. '
