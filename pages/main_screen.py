import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainScreen(Page):
    WIDGET_TEXTVIEW = (By.CLASS_NAME, 'android.widget.TextView')
    WIDGET_EDITTEXT = (By.CLASS_NAME, 'android.widget.EditText')
    BUTTON_MENU_EU = "Menu"
    BUTTON_ADD_NEW_EU = "Add new +"
    BUTTON_ADD_PHOTO_CATEGORY_EU = "Add photo"
    CATEGORY_NAME_EU = "Pizza"
    BUTTON_SAVE_CATEGORY_XPAHT_EU = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView")
    CATEGORY_NAME_INPUT_XPAHT_EU = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")
    BUTTON_SAVE_CATEGORY_OK_XPAHT_EU = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView")

    def click_on_button_menu_eu(self):
        self.find_elements_and_click(self.BUTTON_MENU_EU, *self.WIDGET_TEXTVIEW)

    def clicking_on_the_button_will_add_eu(self):
        self.find_elements_and_click(self.BUTTON_ADD_NEW_EU, *self.WIDGET_TEXTVIEW)

    def click_add_photo_category_eu(self):
        self.find_elements_and_click(self.BUTTON_ADD_PHOTO_CATEGORY_EU, *self.WIDGET_TEXTVIEW)

    def press_the_button_with_choose_from_library_eu(self):
        TouchAction(self.driver).tap(x=100, y=1328).perform()
        time.sleep(1)

    def click_google_photos_eu(self):
        TouchAction(self.driver).tap(x=119, y=1173).perform()
        time.sleep(1)

    def click_on_the_downloads_folder_eu(self):
        TouchAction(self.driver).tap(x=174, y=498).perform()
        time.sleep(1)

    def select_photo_eu(self):
        TouchAction(self.driver).tap(x=130, y=400).perform()
        time.sleep(2)

    def input_category_name_eu(self):
        self.input_line_xpath(self.CATEGORY_NAME_EU, *self.CATEGORY_NAME_INPUT_XPAHT_EU)
        time.sleep(1)

    def click_save_category_eu(self):
        self.click_button_xpath(*self.BUTTON_SAVE_CATEGORY_XPAHT_EU)
        time.sleep(7)

    def click_button_ok_eu(self):
        self.click_button_xpath(*self.BUTTON_SAVE_CATEGORY_OK_XPAHT_EU)
