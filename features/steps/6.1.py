from behave import given, when, then


@given('Tap on application language EU 6.1')
def selection_language(context):
    context.app.login_page.selection_language_eu()
    context.app.login_page.i_agree()


@when('Enter email EU 6.1')
def enter_email(context):
    context.app.login_page.input_email()


@when('Enter password EU 6.1')
def enter_pass(context):
    context.app.login_page.input_pass()


@when('Click on the "Sign in" button EU 6.1')
def click_button_sign_in(context):
    context.app.login_page.click_button_sign_in()


@when('Profile page is open EU 6.1')
def login_page_is_open_eu(context):
    context.app.login_page.profile_page_is_open_eu()


@when('Press the add event button EU 6.1')
def press_the_add_event_button_eu(context):
    context.app.main_screen.click_on_button_add_event_eu()