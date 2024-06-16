class Header:
    @staticmethod
    def pivot_xpath():
        return '//*[@id="global_header"]'

    def login_button(self):
        return self.pivot_xpath() + '//div[@id="global_action_menu"]/a[2]'
