from config import LINK
from flows.common import HeaderFlows
from flows.auth_page import AuthFlows
from utils.utils import BaseActions as BaseA
from containers.auth_page import LoginPage
from config import STEAM_LOGIN, STEAM_PASSWORD

ERRORS_LIST = ['Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.',
               'Please check your password and account name and try again.']


def test_google_search(browser):
    browser.get(LINK)
    HeaderFlows.click_to_login_button(browser)
    AuthFlows.enter_account_name(browser, STEAM_LOGIN)
    AuthFlows.enter_password(browser, STEAM_PASSWORD)
    AuthFlows.click_login_btn(browser)
    assert BaseA.find_element(browser, LoginPage.error_msg()).text in ERRORS_LIST
