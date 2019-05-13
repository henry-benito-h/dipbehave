import json
from compare import expect, ensure
from behave import *
from jsonschema import validate

from transformation.param_transformation import replace_parameters

use_step_matcher("re")


@step(u'I have the next endpoint "(?P<endpoint>.*)"')
def step_impl(context, endpoint):
    if '<id>' in endpoint and hasattr(context, 'id'):
        endpoint = endpoint.replace('<id>', str(context.id))
    context.endpoint = endpoint


@step(u'I have the body payload below')
def step_impl(context):
    try:
        new_context_text = replace_parameters(context.text)
    except AttributeError:
        ensure(False, True, "There was an error on parameters values, please review custom method names")
    context.req_body_dict = json.loads(new_context_text)
    context.req_body = json.dumps(context.req_body_dict)
    context.vars.update({context.endpoint: context.req_body_dict})
    # context.vars.update({f"{context.endpoint}.{context.req_body.get('name')}" : context.req_body})


@step(u'I do an api (?P<method>GET|POST|PUT|DELETE) request')
def step_impl(context, method):
    data = context.req_body if hasattr(context, 'req_body') else None
    params = context.req_params if hasattr(context, 'req_params') else None
    context.response = context.request.call(method, context.endpoint, data=data, params=params)


@step(u'I should have (?P<status_code>.*) as status code')
def step_impl(context, status_code):
    expect(int(status_code)).to_equal(context.response.status_code)


@step("response body should match with (?P<content>.*)?content")
def step_impl(context, content):
    content = content.rstrip()
    if content == "empty" and context.text:
        ensure(False, True, "If we are waiting 'empty content' should not exist a text below the step")

    if context.text is None:
        expect("").to_equal(context.response.text)

    if context.text:
        new_context_text = replace_parameters(context.text)
        try:
            current = context.response.json()
            if content:
                current = current[content][0]
            expected = json.loads(new_context_text)
            for key in expected:
                expect(expected[key]).to_equal(current[key])
        except KeyError:
            ensure(False, True, "This key '{}' does not exist for both dicts".format(key))


@step("I have a record already created with this content")
def step_impl(context):
    new_context_text = replace_parameters(context.text)
    params = context.req_params if hasattr(context, 'req_params') else None
    request_response = context.request.call('POST', context.endpoint, data=new_context_text, params=params)
    context.id = request_response.json()["id"]


@given('I am authenticated as "(?P<credentials>.*)"')
def step_impl(context, credentials):
    try:
        context.request.update_credentials(credentials)
        endpoint = "me?fields=accounts(id)"
        context.my_id = context.request.call('GET', endpoint, data=None, params=None).json()["accounts"][0]["id"]
    except KeyError:
        ensure(False, True, "Wrong credential value. Key '{}' does not exist".format(credentials))


@then(u'The response body should have an id')
def step_impl(context):
    result = context.response.json()
    expect(result).to_be_truthy()
    expect(result['id']).to_be_truthy()


@step("I remove all projects from dashboard")
def step_impl(context):
    all_projects = context.request.call('GET', 'projects');
    all_projects = all_projects.json();
    for project in all_projects:
        print(project['id'])
        all_projects = context.request.call('DELETE', f"projects/{project['id']}");


@step("the response body should contain previous content(?: and)?")
def step_impl(context):
    if context.text:
        text_replaced = replace_parameters(context.text)
        expected = json.loads(text_replaced)
        new_expected = {**context.vars.get(context.endpoint), **expected}
    else:
        new_expected = context.vars.get(context.endpoint)
    current_response = context.response.json()
    for key in new_expected:
        expect(new_expected[key]).to_equal(current_response[key])


@step("the response body should be equal to GET body")
def step_impl(context):
    current_response = context.response.json()
    if "/" in context.endpoint:
        get_response = context.request.call('GET', context.endpoint).json()
    else:
        get_response = context.request.call('GET', f"{context.endpoint}/{current_response['id']}").json()

    expect(current_response).to_equal(get_response)


@step('I create a record for "(?P<endpoint_name>.*)" from template')
def step_impl(context, endpoint_name):
    template = open(f"resources/templates/{endpoint_name}.json")
    new_context_text = replace_parameters(template.read())
    new_context_text = json.dumps(json.loads(new_context_text))
    params = context.req_params if hasattr(context, 'req_params') else None
    request_response = context.request.call('POST', endpoint_name, data=new_context_text, params=params)
    context.id = request_response.json()["id"]
    pass


@step("I verify response schema")
def step_impl(context):
    current_response = context.response.json()
    expected_schema = json.loads(context.text)
    validate(instance=current_response, schema=expected_schema)
