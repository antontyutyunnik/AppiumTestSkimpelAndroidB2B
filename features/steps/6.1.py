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


@when('Click add photo EU 6.1')
def click_add_photo_category_eu(context):
    context.app.event_page.click_add_photo_category_eu()


@when('Press the button with Choose from Library EU 6.1')
def press_the_button_with_choose_from_library_eu(context):
    context.app.event_page.press_the_button_with_choose_from_library_eu()


@when('Click Google Photos EU 6.1')
def click_google_photos_eu(context):
    context.app.event_page.click_google_photos_eu()


@when('Click on the Downloads folder EU 6.1')
def click_on_the_downloads_folder(context):
    context.app.event_page.click_on_the_downloads_folder_eu()


@when('Select photo EU 6.1')
def select_photo(context):
    context.app.event_page.select_photo_eu()

@when('Enter the name of the event EU 6.1')
def input_headline_event_eu(context):
    context.app.event_page.input_headline_event_eu()

@when('Enter event description EU 6.1')
def input_description_event_eu(context):
    context.app.event_page.input_description_event_eu()

@when('Enter event date EU 6.1')
def click_on_date_eu(context):
    context.app.event_page.click_on_date_eu()

@when('Enter event time EU 6.1')
def click_on_time_eu(context):
    context.app.event_page.click_on_time_eu()

@when('Enter event price EU 6.1')
def input_price_event_eu(context):
    context.app.event_page.input_price_event_eu()

@when('Click Save EU 6.1')
def click_save_event_eu(context):
    context.app.event_page.click_save_event_eu()


@then('Click OK EU 6.1')
def click_save_event_ok_eu(context):
    context.app.event_page.click_save_event_ok_eu()
