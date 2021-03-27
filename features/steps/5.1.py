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


@when('Profile page is open EU 5.1')
def login_page_is_open_eu(context):
    context.app.login_page.profile_page_is_open_eu()


@when('Press the menu button EU 5.1')
def press_the_menu_button_eu(context):
    context.app.main_screen.click_on_button_menu_eu()


@when('Clicking on the button will add EU 5.1')
def press_the_menu_button_eu(context):
    context.app.main_screen.clicking_on_the_button_will_add_eu()


@when('Click add photo EU 5.1')
def click_add_photo_category_eu(context):
    context.app.main_screen.click_add_photo_category_eu()


@when('Press the button with Choose from Library EU 5.1')
def press_the_button_with_choose_from_library_eu(context):
    context.app.main_screen.press_the_button_with_choose_from_library_eu()
