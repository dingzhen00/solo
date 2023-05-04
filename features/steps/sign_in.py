from behave import given, when, then
from django.urls import reverse
from django.test.client import Client

@given('I am on the "sign-in" page')
def step_impl(context):
    context.client = Client()
    context.response = context.client.get(reverse('sign_in'))
    assert context.response.status_code == 200

@when('I enter "{username}" as the username')
def step_impl(context, username):
    context.username = username
    context.response = context.client.post(reverse('sign_in'), {
        'username': context.username,
        'password': context.password,
        'csrfmiddlewaretoken': context.client.cookies['csrftoken'].value,
    }, follow=True)
    assert context.response.status_code == 200

@when('I enter "{password}" as the password')
def step_impl(context, password):
    context.password = password

@when('I click the "Submit" button')
def step_impl(context):
    context.response = context.client.post(reverse('sign_in'), {
        'username': context.username,
        'password': context.password,
        'csrfmiddlewaretoken': context.client.cookies['csrftoken'].value,
    }, follow=True)
    assert context.response.status_code == 200

@then('I should be redirected to the "product-list" page')
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.resolver_match.url_name == 'product_list'

@then('I should see an error message')
def step_impl(context):
    assert context.response.status_code == 200
    assert 'alert-danger' in context.response.content.decode()

@when('I leave the username or password field blank')
def step_impl(context):
    context.response = context.client.post(reverse('sign_in'), {
        'username': '',
        'password': context.password,
        'csrfmiddlewaretoken': context.client.cookies['csrftoken'].value,
    }, follow=True)
    assert context.response.status_code == 200 or 'alert-danger' in context.response.content.decode()

