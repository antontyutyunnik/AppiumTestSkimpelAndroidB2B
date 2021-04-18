import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page


class EventPage(Page):
    WIDGET_TEXTVIEW = (By.CLASS_NAME, 'android.widget.TextView')
    WIDGET_EDITTEXT = (By.CLASS_NAME, 'android.widget.EditText')
    BUTTON_ADD_PHOTO_CATEGORY_EU = "Add photo"
    EVENT_NAME = "A party is a gathering of people who have been invited by a host for the purposes of socializing"
    EVENT_NAME_LINE = "Enter a title"
    PRICE_LINE = "€12"
    PRICE = "10"
    EVENT_DESCRIPTION = "Some parties are held in honor of a specific person, day, or event, such as a birthday party, a Super Bowl party, or a St. Patrick’s Day party. Parties of this kind are often called celebrations. A party is not necessarily a private occasion. Public parties are sometimes held in restaurants, pubs, beer gardens, nightclubs or bars, and people attending such parties may be charged an admission fee by the host. Large parties in public streets may celebrate events such as Mardi Gras or the signing of a peace treaty ending a long war."
    EVENT_DESCRIPTION_LINE = "Enter a description"
    BUTTON_SAVE_EVENT_OK_XPAHT = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView")
    BUTTON_SAVE_XPAHT = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[8]/android.widget.TextView")
    TIME_LINE_XPAHT = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.TextView")
    DATA_LINE_XPAHT = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView")

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

    def input_headline_event_eu(self):
        time.sleep(2)
        self.input(self.EVENT_NAME_LINE, self.EVENT_NAME, *self.WIDGET_EDITTEXT)

    def input_description_event_eu(self):
        time.sleep(2)
        self.input(self.EVENT_DESCRIPTION_LINE, self.EVENT_DESCRIPTION, *self.WIDGET_EDITTEXT)
        time.sleep(1)
        self.driver.swipe(324, 1268, 343, 561, 400)

    def click_on_date_eu(self):
        time.sleep(2)
        self.click_button_xpath(*self.DATA_LINE_XPAHT)
        time.sleep(2)
        self.driver.swipe(197, 843, 197, 611, 400)
        time.sleep(1)
        TouchAction(self.driver).tap(x=520, y=990).perform()

    def click_on_time_eu(self):
        time.sleep(2)
        self.click_button_xpath(*self.TIME_LINE_XPAHT)
        time.sleep(2)
        self.driver.swipe(284, 838, 279, 597, 400)
        time.sleep(1)
        TouchAction(self.driver).tap(x=450, y=990).perform()

    def input_price_event_eu(self):
        time.sleep(2)
        self.input(self.PRICE_LINE, self.PRICE, *self.WIDGET_EDITTEXT)

    def click_save_event_eu(self):
        time.sleep(2)
        self.click_button_xpath(*self.BUTTON_SAVE_XPAHT)
        time.sleep(4)

    def click_save_event_ok_eu(self):
        time.sleep(2)
        self.click_button_xpath(*self.BUTTON_SAVE_EVENT_OK_XPAHT)
        time.sleep(8)