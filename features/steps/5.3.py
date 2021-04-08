from behave import given, when, then


@given('Tap on application language EU 5.3')
def selection_language(context):
    context.app.login_page.selection_language_eu()
    context.app.login_page.i_agree()


@when('Enter email EU 5.3')
def enter_email(context):
    context.app.login_page.input_email()


@when('Enter password EU 5.3')
def enter_pass(context):
    context.app.login_page.input_pass()


@when('Click on the "Sign in" button EU 5.3')
def click_button_sign_in(context):
    context.app.login_page.click_button_sign_in()


@when('Profile page is open EU 5.3')
def login_page_is_open_eu(context):
    context.app.login_page.profile_page_is_open_eu()


@when('Press the menu button EU 5.3')
def press_the_menu_button_eu(context):
    context.app.main_screen.click_on_button_menu_eu()


@when('Press the category name EU 5.3')
def press_the_category_name_eu(context):
    context.app.menu_page.click_on_category_name_eu()


@when('Clicking on the button will add EU 5.3')
def press_the_menu_button_eu(context):
    context.app.menu_page.clicking_on_the_button_will_add_eu()


@when('Click add photo EU 5.3')
def click_add_photo_category_eu(context):
    context.app.menu_page.click_add_photo_category_eu()


@when('Press the button with take photo EU 5.3')
def press_the_button_with_choose_from_library_eu(context):
    context.app.menu_page.press_the_button_with_take_photo_eu()


@when('Press the button allow EU 5.3')
def press_the_button_with_choose_from_library_eu(context):
    context.app.menu_page.press_the_button_allow_eu()


@when('Press the button take photo EU 5.3')
def press_the_button_take_photo_eu(context):
    context.app.menu_page.press_the_button_take_photo_eu()


@when('Press the button take photo ok EU 5.3')
def press_the_button_take_photo_ok_eu(context):
    context.app.menu_page.press_the_button_take_photo_ok_eu()


@when('Input product name EU 5.3')
def input_product_name_eu(context):
    context.app.menu_page.input_product_name_eu()


@when('Input description product name EU 5.3')
def input_product_description_eu(context):
    context.app.menu_page.input_description_product()


@when('Input product price  EU 5.3')
def input_product_price_eu(context):
    context.app.menu_page.input_price_product()


@when('Input product weight EU 5.3')
def input_product_price_eu(context):
    context.app.menu_page.input_weight_product()


@when('Click save EU 5.3')
def select_photo(context):
    context.app.menu_page.click_save_category_eu()


@then('Click button ok EU 5.3')
def select_photo(context):
    context.app.menu_page.click_button_ok_eu()
