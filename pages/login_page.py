import time
from selenium.webdriver.common.by import By
from pages.base_page import Page


class LoginPage(Page):
    WIDGET_TEXTVIEW = (By.CLASS_NAME, 'android.widget.TextView')
    WIDGET_EDITTEXT = (By.CLASS_NAME, 'android.widget.EditText')
    LANGUAGE_EN_TEXT = "Use English"
    LANGUAGE_DE_TEXT = "Verwenden Sie Deutsch"
    I_AGREE_BUTTON_EU = "I agree with the rules"
    I_AGREE_BUTTON_DE = "Ich stimme den Regeln zu"
    EMAIL_INPUT = "Example@gmail.com"
    EMAIL = "antontyutyunnik93@gmail.com"
    EMAIL_BAD = "antontyutyunnik9333@gmail.com"
    EMAIL_OR_PASS_NOT_CORRECT = "Email or password not correct"
    PASS_INPUT = "••••••••"
    PASS = "123qqq"
    PASS_BAD = "123qqqBAD"
    SIGN_IN = "Sign in"
    SIGN_IN_XPAHT = (By.XPATH, "//android.view.ViewGroup[@content-desc='btn-signIn']/android.view.View")
    EMAIL_OR_PASS_NOT_CORRECT_XPAHT = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[2]")
    EINLOGGEN = "Einloggen"
    PROFILE = "Profile"

    def selection_language_eu(self):
        self.find_elements_and_click(self.LANGUAGE_EN_TEXT, *self.WIDGET_TEXTVIEW)

    def selection_language_de(self):
        self.find_elements_and_click(self.LANGUAGE_DE_TEXT, *self.WIDGET_TEXTVIEW)

    def i_agree(self):
        self.driver.swipe(324, 1268, 343, 561, 400)
        self.find_elements_and_click(self.I_AGREE_BUTTON_EU, *self.WIDGET_TEXTVIEW)

    def scroll_down_i_agree(self):
        self.driver.swipe(324, 1268, 343, 561, 400)

    def click_on_button_i_agree_eu(self):
        self.find_elements_and_click(self.I_AGREE_BUTTON_EU, *self.WIDGET_TEXTVIEW)

    def click_on_button_i_agree_de(self):
        self.find_elements_and_click(self.I_AGREE_BUTTON_DE, *self.WIDGET_TEXTVIEW)

    def input_email(self):
        self.input(self.EMAIL_INPUT, self.EMAIL, *self.WIDGET_EDITTEXT)

    def input_email_bad(self):
        self.input(self.EMAIL_INPUT, self.EMAIL_BAD, *self.WIDGET_EDITTEXT)

    def input_pass(self):
        self.input(self.PASS_INPUT, self.PASS, *self.WIDGET_EDITTEXT)

    def input_pass_bad(self):
        self.input(self.PASS_INPUT, self.PASS_BAD, *self.WIDGET_EDITTEXT)

    def click_button_sign_in(self):
        self.click_button(self.SIGN_IN, *self.WIDGET_TEXTVIEW)

    def click_button_sign_in_xpath(self):
        self.click_button_xpath(*self.SIGN_IN_XPAHT)

    def profile(self):
        time.sleep(5)
        self.find_elements(self.PROFILE, *self.WIDGET_TEXTVIEW)

    def login_page_is_open_eu(self):
        time.sleep(2)
        e = self.find_element(self.SIGN_IN, *self.WIDGET_TEXTVIEW)
        if e == self.SIGN_IN:
            print("login page is open")
        else:
            quit()

    def login_page_is_open_de(self):
        time.sleep(2)
        e = self.find_element(self.EINLOGGEN, *self.WIDGET_TEXTVIEW)
        if e == self.EINLOGGEN:
            print("login page is open")
        else:
            quit()

    def profile_page_is_open_eu(self):
        time.sleep(2)
        e = self.find_element(self.PROFILE, *self.WIDGET_TEXTVIEW)
        if e == self.PROFILE:
            print("Profile page is open")
        else:
            quit()

    def email_or_password_is_not_correct_eu(self):
        time.sleep(2)
        e = self.find_element(self.EMAIL_OR_PASS_NOT_CORRECT, *self.WIDGET_TEXTVIEW)
        if e == self.EMAIL_OR_PASS_NOT_CORRECT:
            print("Email or password not correct")
        else:
            quit()
