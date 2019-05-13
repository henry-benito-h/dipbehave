import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../utils'))
from authorization.authorization_factory import AuthFactory
from utils.request_manager import Request

config = {
    'host': 'https://www.pivotaltracker.com',
    'root_path': '/services/v5/',
    'authorization_type': 'bearer',
    'default_role': 'admin',
    'headers': {
        'accept': 'application/json',
        'Content-Type': 'application/json'},
    'roles': {
        'admin': {
            'username': 'admin',
            'password': 'admin',
            'headers': {
                'X-TrackerToken': 'e0b6db9c0cc59332f65349b85a6a3b26'
            }
        }
    }
}

wrong_config = {
    'host': 'https://www.pivotaltracker.com',
    'root_path': '/services/v5/',
    'authorization_type': 'bearer',
    'default_role': 'admin',
    'headers': {
        'accept': 'application/json',
        'Content-Type': 'application/json'},
    'roles': {
        'admin': {
            'usrname': 'admin',
            'passd': 'admin',
            'headers': {
                'X-TracerToken': 'e0b6db9c0cc59332f65349b85a6a3b26'
            }
        }
    }
}


def test_basic_authorization():
    auth_factory = AuthFactory()
    request = Request(config)
    auth_type = auth_factory.get_auth("basic")()
    auth_type.load_config(request, request.role)
    assert str(type(request.auth)) == "<class 'requests.auth.HTTPBasicAuth'>"
    assert request.auth.username == request.role["username"]
    assert request.auth.password == request.role["password"]
    assert "X-TrackerToken" not in list(request.headers.keys())


def test_bearer_authorization():
    auth_factory = AuthFactory()
    request = Request(config)
    auth_type = auth_factory.get_auth("bearer")()
    auth_type.load_config(request, request.role)
    assert request.auth is None
    for header in request.role["headers"]:
        assert request.role["headers"][header] == request.headers[header]


def test_wrong_config_basic_authorization():
    auth_factory = AuthFactory()
    request = Request(wrong_config)
    auth_type = auth_factory.get_auth("basic")()
    assert auth_type.load_config(request, request.role) is None


def test_wrong_config_bearer_authorization():
    auth_factory = AuthFactory()
    request = Request(wrong_config)
    auth_type = auth_factory.get_auth("bearer")()
    assert auth_type.load_config(request, request.role) is None
    pass
