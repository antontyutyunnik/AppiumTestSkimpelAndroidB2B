from behave import given, when, then


@given('Tap on application language')
def selection_language(context):
    context.app.login_page.selection_language()
    context.app.login_page.i_agree()


@when('Enter Email and Password and click on Sign in')
def enter_email_and_pass(context):
    context.app.login_page.input_email()
    context.app.login_page.input_pass()
    context.app.login_page.click_button_sign_in()


@then('Show account User')
def show_account_user(context):
    context.app.login_page.profile()
