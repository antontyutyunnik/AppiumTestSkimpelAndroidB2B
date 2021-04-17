import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainScreen(Page):
    WIDGET_TEXTVIEW = (By.CLASS_NAME, 'android.widget.TextView')
    WIDGET_EDITTEXT = (By.CLASS_NAME, 'android.widget.EditText')
    BUTTON_MENU_EU = "Menu"
    BUTTON_ADD_EVENT_EU = "Add event"
    BUTTON_EDIT_PROFILE_EU = "Edit profile"
    BUTTON_ADD_NEW_EU = "Add new +"
    BUTTON_ADD_PHOTO_CATEGORY_EU = "Add photo"
    CATEGORY_NAME_EU = "Pizza"
    BUTTON_SAVE_CATEGORY_XPAHT_EU = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView")
    CATEGORY_NAME_INPUT_XPAHT_EU = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")
    BUTTON_SAVE_CATEGORY_OK_XPAHT_EU = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView")

    def click_on_button_menu_eu(self):
        self.find_elements_and_click(self.BUTTON_MENU_EU, *self.WIDGET_TEXTVIEW)
        time.sleep(1)

    def click_on_button_edit_profile_eu(self):
        self.find_elements_and_click(self.BUTTON_EDIT_PROFILE_EU, *self.WIDGET_TEXTVIEW)

    def click_on_button_add_event_eu(self):
        self.find_elements_and_click(self.BUTTON_ADD_EVENT_EU, *self.WIDGET_TEXTVIEW)

