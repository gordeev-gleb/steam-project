from selenium.webdriver.common.by import By
from utils.utils import BaseActions as BaseA


class Header:
    pivot_xpath = '//*[@id="global_header"]'
    login_button = f'{pivot_xpath}//div[@id="global_action_menu"]/a[2]'

    @staticmethod
    def click_to_login_button(browser):
        return BaseA.find_element(browser, Header.login_button).click()
