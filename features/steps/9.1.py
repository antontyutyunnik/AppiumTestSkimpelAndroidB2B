from behave import given, when, then


@given('Tap on application language EU 9.1')
def selection_language(context):
    context.app.login_page.selection_language_eu()
    context.app.login_page.i_agree()


@when('Enter email EU 9.1')
def enter_email(context):
    context.app.login_page.input_email()


@when('Enter password EU 9.1')
def enter_pass(context):
    context.app.login_page.input_pass()


@when('Click on the "Sign in" button EU 9.1')
def click_button_sign_in(context):
    context.app.login_page.click_button_sign_in()


@when('Profile page is open EU 9.1')
def login_page_is_open_eu(context):
    context.app.login_page.profile_page_is_open_eu()

@when('Press the edit profile button EU 9.1')
def press_the_edit_profile_button_eu(context):
    context.app.main_screen.click_on_button_edit_profile_eu()

@when('Scroll down edit profile 9.1')
def scroll_down_edit_profile(context):
    context.app.edit_profile_page.scroll_down_edit_profile()

@when('Press button delete account EU 9.1')
def click_button_delete_account(context):
    context.app.edit_profile_page.click_button_delete_account()