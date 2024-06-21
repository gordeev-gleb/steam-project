from flows.main_page import MainPage
from flows.auth_page import LoginPage
from utils.wait_utils import WaitUtils
from utils.json_utils import JSON


def test_login_error(browser):
    # Переходим с основной страницы на страницу авторизации
    main_page = MainPage(browser)
    main_page.click_to_login_button()
    # Проходим авторизацию
    login_page = LoginPage(browser)
    login_page.login(JSON.get_credentials('STEAM_LOGIN'), JSON.get_credentials('STEAM_PASSWORD'))
    check_error = WaitUtils.wait_presence_of_element(browser, LoginPage.ERROR_MSG_LOC).text
    assert check_error == 'Please check your password and account name and try again.', \
        f"Error not found or error text is different. Current Error: {check_error}"
