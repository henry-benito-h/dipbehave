import pytest
from utils.authorization_factory import AuthFactory
from utils.request_manager import Request


def test_basic_authorization():
    config = {
        'host': 'https://www.pivotaltracker.com',
        'root_path': '/services/v5/', 'auth': 'bearer',
        'headers': {'accept': 'application/json',
                    'Content-Type': 'application/json'
                    },
        'roles': {
            'admin': {
                'username': 'admin',
                'password': 'admin',
                'token_header': 'X-TrackerToken',
                'token': 'e0b6db9c0cc59332f65349b85a6a3b26'
            }
        }
    }
    auth_factory = AuthFactory()
    request = Request(config)
    role = config["roles"]["admin"]
    auth_type = auth_factory.get_auth("basic")(request, role)
    auth_type.set_params()
    assert str(type(request.auth)) == "<class 'requests.auth.HTTPBasicAuth'>"
    assert request.auth.username == role["username"]
    assert request.auth.password == role["password"]
    assert role["token_header"] not in request.headers


def sum_numbers(num1, num2):
    """It returns sum of two numbers"""
    return num1 + num2