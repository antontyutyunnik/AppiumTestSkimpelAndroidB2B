from behave import given, when, then


@given('Tap on application language EU 3.1')
def selection_language(context):
    context.app.login_page.selection_language_eu()
    context.app.login_page.i_agree()

@when('Click on the Sign up button on login page EU 3.1')
def click_on_the_sign_up_button_eu(context):
    context.app.login_page.click_button_sign_up_xpath()

@when('Enter email EU 3.1')
def enter_email_eu(context):
    context.app.login_page.input_email_registration()

@when('Enter password EU 3.1')
def enter_email_eu(context):
    context.app.login_page.input_pass_registration()

@when('Enter company name EU 3.1')
def enter_company_name_eu(context):
    context.app.login_page.input_company_name()

@when('Select category company EU 3.1')
def select_category_company_eu(context):
    context.app.login_page.select_category_company()

@when('Click button done EU 3.1')
def click_button_done_eu(context):
    context.app.login_page.click_button_done()

@when('Click add address EU 3.1')
def click_button_add_address_eu(context):
    context.app.login_page.click_button_add_address()

@when('At search enter address Belziger 19 EU 3.1')
def at_search_enter_address_eu(context):
    context.app.login_page.input_search_address_for_registration()

@when('Address select from list EU 3.1')
def at_search_enter_address_eu(context):
    context.app.login_page.address_select_from_list_registration()

@then('Click button Sign up on registration page EU 3.1')
def click_button_sign_up_on_registration_page_eu(context):
    context.app.login_page.click_button_sign_up_on_registration_page_eu()
    context.app.login_page.online_payments_page_is_open_eu()