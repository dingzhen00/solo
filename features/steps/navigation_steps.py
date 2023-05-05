from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@step('I am on the homepage')
def step_i_am_on_the_homepage(context):
    context.browser.get(context.base_url)

@step('I click on "{link_text}"')
def step_i_click_on(context, link_text):
    link = WebDriverWait(context.browser, 3).until(
        EC.presence_of_element_located((By.LINK_TEXT, link_text))
    )
    link.click()


@step('I should be on the registration page')
def step_i_should_be_on_registration_page(context):
    assert 'Registration' in context.browser.title

@step('I should be on the login page')
def step_i_should_be_on_login_page(context):
    assert 'Login' in context.browser.title

@step('I should be on the admin login page')
def step_i_should_be_on_admin_login_page(context):
    assert 'Admin Login' in context.browser.title

@step('I go back to the homepage')
def step_i_go_back_to_the_homepage(context):
    context.browser.get(context.base_url)





