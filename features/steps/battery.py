import requests
from behave import *
from hamcrest import *

@given(u'the battery calculation module is online and available')
def step_impl(context):
    context.url = "http://dingdata.nl/batterij"

@when(u'I call the battery calculation module with {UK} and {RL}')
def step_impl(context, UK, RL):
    context.request = requests.get(url = context.url, params = {'UK': UK, 'RL': RL})

@then(u'The module calculates the correct value of {I}')
def step_impl(context, I):
    response = context.request.json()
    answer = response["resultaten"]["antwoord"]
    float_answer = answer[4:8]
    assert_that(float(float_answer), equal_to(float(I)))