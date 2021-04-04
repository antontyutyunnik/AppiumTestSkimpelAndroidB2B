from pages.login_page import LoginPage
from pages.main_screen import MainScreen
from pages.menu_page import MenuPage
from pages.edit_profile_page import EditProfilePage


class Application:

    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.main_screen = MainScreen(driver)
        self.menu_page = MenuPage(driver)
        self.edit_profile_page = EditProfilePage(driver)
