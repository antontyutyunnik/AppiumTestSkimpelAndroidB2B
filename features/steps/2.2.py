from behave import given, when, then


@given('Tap on application language EU 2.2')
def selection_language(context):
    context.app.login_page.selection_language_eu()
    context.app.login_page.i_agree()


@when('Enter email EU 2.2')
def enter_email(context):
    context.app.login_page.input_email_bad()


@when('Enter password EU 2.2')
def enter_pass(context):
    context.app.login_page.input_pass()


@then('Click on the "Sign in" button EU 2.2')
def click_button_sign_in(context):
    context.app.login_page.click_button_sign_in_xpath()


@then('Email or password is not correct EU 2.2')
def login_page_is_open_eu(context):
    context.app.login_page.email_or_password_is_not_correct_eu()