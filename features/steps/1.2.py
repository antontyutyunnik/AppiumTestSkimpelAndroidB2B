from behave import given, when, then

@given('Tap on application language DE 1.2')
def selection_language(context):
    context.app.login_page.selection_language_de()

@when('Scroll to the bottom of the page DE 1.2')
def scroll_down_i_agree(context):
    context.app.login_page.scroll_down_i_agree()

@when('Click on the button "I agree" DE 1.2')
def click_on_button_i_agree(context):
    context.app.login_page.click_on_button_i_agree_de()

@then('login page is open DE 1.2')
def click_on_button_i_agree(context):
    context.app.login_page.login_page_is_open_de()