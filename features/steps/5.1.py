from behave import given, when, then


@given('Tap on application language EU 5.1')
def selection_language(context):
    context.app.login_page.selection_language_eu()
    context.app.login_page.i_agree()


@when('Enter email EU 5.1')
def enter_email(context):
    context.app.login_page.input_email()


@when('Enter password EU 5.1')
def enter_pass(context):
    context.app.login_page.input_pass()


@when('Click on the "Sign in" button EU 5.1')
def click_button_sign_in(context):
    context.app.login_page.click_button_sign_in()


@then('Profile page is open EU 5.1')
def login_page_is_open_eu(context):
    context.app.login_page.profile_page_is_open_eu()