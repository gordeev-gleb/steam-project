from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class WebDriverSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WebDriverSingleton, cls).__new__(cls)
            cls._instance.driver = None
        return cls._instance

    def get_driver(self, language):
        if self.driver is None:
            service = Service(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            options.add_argument(f"--lang={language}")
            self.driver = webdriver.Chrome(service=service, options=options)
        return self.driver

    def quit_driver(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
