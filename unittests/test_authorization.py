import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../utils'))
from authorization.authorization_factory import AuthFactory
from utils.request_manager import Request

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
wrong_config = {
    'host': 'https://www.pivotaltracker.com',
    'root_path': '/services/v5/', 'auth': 'bearer',
    'headers': {'accept': 'application/json',
                'Content-Type': 'application/json'
                },
    'roles': {
        'admin': {
            'usrname': 'admin',
            'pssword': 'admin',
            'token_heade': 'X-TrackerToken',
            'tokn': 'e0b6db9c0cc59332f65349b85a6a3b26'
        }
    }
}


def test_basic_authorization():
    auth_factory = AuthFactory()
    request = Request(config)
    role = config["roles"]["admin"]
    auth_type = auth_factory.get_auth("basic")(request, role)
    auth_type.set_params()
    assert str(type(request.auth)) == "<class 'requests.auth.HTTPBasicAuth'>"
    assert request.auth.username == role["username"]
    assert request.auth.password == role["password"]
    assert role["token_header"] not in request.headers


def test_bearer_authorization():
    auth_factory = AuthFactory()
    request = Request(config)
    role = config["roles"]["admin"]
    auth_type = auth_factory.get_auth("bearer")(request, role)
    auth_type.set_params()
    assert request.auth is None
    assert request.headers[role["token_header"]] == role["token"]


def test_wrong_config_basic_authorization():
    auth_factory = AuthFactory()
    request = Request(wrong_config)
    role = wrong_config["roles"]["admin"]
    auth_type = auth_factory.get_auth("basic")(request, role)
    assert auth_type.set_params() is None


def test_wrong_config_bearer_authorization():
    auth_factory = AuthFactory()
    request = Request(wrong_config)
    role = wrong_config["roles"]["admin"]
    auth_type = auth_factory.get_auth("bearer")(request, role)
    assert auth_type.set_params() is None
