from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainScreen(Page):
    WIDGET_TEXTVIEW = (By.CLASS_NAME, 'android.widget.TextView')
    WIDGET_EDITTEXT = (By.CLASS_NAME, 'android.widget.EditText')
    BUTTON_MENU_EU = "Menu"
    BUTTON_ADD_NEW_EU = "Add new +"
    BUTTON_ADD_PHOTO_CATEGORY_EU = "Add photo"

    def click_on_button_menu_eu(self):
        self.find_elements_and_click(self.BUTTON_MENU_EU, *self.WIDGET_TEXTVIEW)

    def clicking_on_the_button_will_add_eu(self):
        self.find_elements_and_click(self.BUTTON_ADD_NEW_EU, *self.WIDGET_TEXTVIEW)

    def click_add_photo_category_eu(self):
        self.find_elements_and_click(self.BUTTON_ADD_PHOTO_CATEGORY_EU, *self.WIDGET_TEXTVIEW)

    def press_the_button_with_choose_from_library_eu(self):
        self.driver.tap("x", "y")
