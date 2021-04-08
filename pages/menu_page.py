import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page


class MenuPage(Page):
    WIDGET_TEXTVIEW = (By.CLASS_NAME, 'android.widget.TextView')
    WIDGET_EDITTEXT = (By.CLASS_NAME, 'android.widget.EditText')
    BUTTON_MENU_EU = "Menu"
    BUTTON_ADD_NEW_EU = "Add new +"
    BUTTON_ADD_PHOTO_CATEGORY_EU = "Add photo"
    CATEGORY_NAME_EU = "Pizza"
    NAME_PRODUCT_EU = "Tomato"
    DESCRIPTION_PRODUCT_EU = "Test description"
    PRICE_PRODUCT_EU = "10"
    WEIGHT_PRODUCT_EU = "500"
    WEIGHT_PRODUCT_XPAHT = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.EditText")
    PRICE_PRODUCT_XPAHT = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.EditText")
    DESCRIPTION_PRODUCT_XPAHT = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText")
    NAME_PRODUCT_LINE_XPAHT = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")
    BUTTON_SAVE_CATEGORY_XPAHT_EU = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView")
    CATEGORY_NAME_INPUT_XPAHT_EU = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")
    BUTTON_SAVE_CATEGORY_OK_XPAHT_EU = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView")

    def clicking_on_the_button_will_add_eu(self):
        time.sleep(2)
        self.find_elements_and_click(self.BUTTON_ADD_NEW_EU, *self.WIDGET_TEXTVIEW)

    def click_on_category_name_eu(self):
        self.find_elements_and_click(self.CATEGORY_NAME_EU, *self.WIDGET_TEXTVIEW)
        time.sleep(2)

    def click_add_photo_category_eu(self):
        time.sleep(2)
        self.find_elements_and_click(self.BUTTON_ADD_PHOTO_CATEGORY_EU, *self.WIDGET_TEXTVIEW)

    def press_the_button_with_choose_from_library_eu(self):
        time.sleep(2)
        TouchAction(self.driver).tap(x=200, y=1340).perform()

    def click_google_photos_eu(self):
        time.sleep(2)
        TouchAction(self.driver).tap(x=119, y=1173).perform()

    def click_on_the_downloads_folder_eu(self):
        time.sleep(2)
        TouchAction(self.driver).tap(x=174, y=498).perform()

    def select_photo_eu(self):
        time.sleep(2)
        TouchAction(self.driver).tap(x=130, y=400).perform()

    def input_category_name_eu(self):
        time.sleep(2)
        self.input_line_xpath(self.CATEGORY_NAME_EU, *self.CATEGORY_NAME_INPUT_XPAHT_EU)

    def click_save_category_eu(self):
        self.click_button_xpath(*self.BUTTON_SAVE_CATEGORY_XPAHT_EU)
        time.sleep(7)

    def click_button_ok_eu(self):
        self.click_button_xpath(*self.BUTTON_SAVE_CATEGORY_OK_XPAHT_EU)

    def press_the_button_with_take_photo_eu(self):
        time.sleep(2)
        TouchAction(self.driver).tap(x=100, y=1220).perform()

    def press_the_button_allow_eu(self):
        time.sleep(2)
        TouchAction(self.driver).tap(x=360, y=850).perform()

    def press_the_button_take_photo_eu(self):
        time.sleep(2)
        TouchAction(self.driver).tap(x=360, y=1350).perform()

    def press_the_button_take_photo_ok_eu(self):
        time.sleep(5)
        TouchAction(self.driver).tap(x=560, y=1350).perform()

    def input_product_name_eu(self):
        time.sleep(2)
        self.input_line_xpath(self.NAME_PRODUCT_EU, *self.NAME_PRODUCT_LINE_XPAHT)

    def input_description_product(self):
        time.sleep(2)
        self.input_line_xpath(self.DESCRIPTION_PRODUCT_EU, *self.DESCRIPTION_PRODUCT_XPAHT)

    def input_price_product(self):
        time.sleep(2)
        self.input_line_xpath(self.PRICE_PRODUCT_EU, *self.PRICE_PRODUCT_XPAHT)

    def input_weight_product(self):
        time.sleep(2)
        self.input_line_xpath(self.WEIGHT_PRODUCT_EU, *self.WEIGHT_PRODUCT_XPAHT)
