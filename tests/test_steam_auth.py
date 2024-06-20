from flows.main_page import MainPage
from flows.auth_page import LoginPage
from utils.utils import WaitUtils, JSON


def test_login_error(browser):
    # Переходим с основной страницы на страницу авторизации
    main_page = MainPage(browser)
    main_page.click_to_login_button()
    # Проходим авторизацию
    login_page = LoginPage(browser)
    login_page.enter_account_name(JSON.get_credentials('STEAM_LOGIN'))
    login_page.enter_password(JSON.get_credentials('STEAM_PASSWORD'))
    login_page.click_login_btn()
    assert WaitUtils.wait_presence_of_element(browser, LoginPage.ERROR_MSG_LOC).text == \
           'Please check your password and account name and try again.', "Error not found or error text is different"
