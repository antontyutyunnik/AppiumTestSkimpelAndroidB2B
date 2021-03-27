from behave import given, when, then


@given('Tap on application language EU 1.1')
def selection_language(context):
    context.app.login_page.selection_language_eu()


@when('Scroll to the bottom of the page EU 1.1')
def scroll_down_i_agree(context):
    context.app.login_page.scroll_down_i_agree()


@when('Click on the button "I agree" EU 1.1')
def click_on_button_i_agree(context):
    context.app.login_page.click_on_button_i_agree_eu()


@then('login page is open EU 1.1')
def click_on_button_i_agree(context):
    context.app.login_page.login_page_is_open_eu()
