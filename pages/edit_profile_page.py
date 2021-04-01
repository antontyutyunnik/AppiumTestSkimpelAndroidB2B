import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page


class EgitProfilePage(Page):
    WIDGET_TEXTVIEW = (By.CLASS_NAME, 'android.widget.TextView')
    WIDGET_EDITTEXT = (By.CLASS_NAME, 'android.widget.EditText')
    BUTTON_DELETE_ACCOUNT = "Delete account"


    def scroll_down_edit_profile(self):
        self.driver.swipe(324, 1268, 343, 561, 400)

    def click_button_delete_account(self):
        self.find_elements_and_click(self.BUTTON_DELETE_ACCOUNT, *self.WIDGET_TEXTVIEW)
