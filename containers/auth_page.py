class LoginPage:
    @staticmethod
    def pivot_xpath():
        return '//*[@data-featuretarget="login"]'

    @staticmethod
    def name_field():
        return LoginPage.pivot_xpath() + '//input[@type="text"]'

    @staticmethod
    def pass_field():
        return LoginPage.pivot_xpath() + '//input[@type="password"]'

    @staticmethod
    def login_btn():
        return LoginPage.pivot_xpath() + '//button[@type="submit"]'

    @staticmethod
    def error_msg():
        return LoginPage.pivot_xpath() + '//form/div[string-length(text()) >15]'
