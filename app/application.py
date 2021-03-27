from pages.login_page import LoginPage
from pages.main_screen import MainScreen


class Application:

    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.main_screen = MainScreen(driver)
