from behave import given, when, then


@given('Tap on application language EU 5.7')
def selection_language(context):
    context.app.login_page.selection_language_eu()
    context.app.login_page.i_agree()


@when('Enter email EU 5.7')
def enter_email(context):
    context.app.login_page.input_email()


@when('Enter password EU 5.7')
def enter_pass(context):
    context.app.login_page.input_pass()


@when('Click on the "Sign in" button EU 5.7')
def click_button_sign_in(context):
    context.app.login_page.click_button_sign_in()


@when('Profile page is open EU 5.7')
def login_page_is_open_eu(context):
    context.app.login_page.profile_page_is_open_eu()


@when('Press the menu button EU 5.7')
def press_the_menu_button_eu(context):
    context.app.main_screen.click_on_button_menu_eu()


@when('Press the category name EU 5.7')
def press_the_category_name_eu(context):
    context.app.menu_page.click_on_category_name_eu()


@when('Clicking on the button will add EU 5.7')
def press_the_menu_button_eu(context):
    context.app.menu_page.clicking_on_the_button_will_add_eu()


@when('Click button edit category EU 5.7')
def click_button_edit_category_eu(context):
    context.app.menu_page.click_button_edit_category()


@when('Click edit category EU 5.7')
def click_edit_category_eu(context):
    context.app.menu_page.click_edit_category()


@when('Input product name EU 5.7')
def input_category_name_burger_eu(context):
    context.app.menu_page.input_category_name_burger_eu()


@then('Click button save EU 5.7')
def click_save_category_eu(context):
    context.app.menu_page.click_save_edit_category_eu()
