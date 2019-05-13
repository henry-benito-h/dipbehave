import sys
import os
import requests

sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from authorization.authorization_factory import AuthFactory


class Request:
    def __init__(self, config):
        self.config = config
        self.auth_factory = AuthFactory()

        self.default_headers = config["headers"].copy()
        self.base_url = f'{config["host"]}{config["root_path"]}'
        self.headers = self.config["headers"]
        self.role = self.get_role()
        self.auth_strategy = self.auth_factory.get_auth(config["authorization_type"])()
        self.auth_strategy.load_config(self, self.role)

    def call(self, method, end_point, **kwargs):
        url = f'{self.base_url}{end_point}'
        return requests.request(method, url, auth=self.auth, headers=self.headers, **kwargs)

    def get(self, end_point, **kwargs):
        return self.call('get', end_point, **kwargs)

    def post(self, end_point, data=None, **kwargs):
        return self.call('post', end_point, data=data, **kwargs)

    def put(self, end_point, data=None, **kwargs):
        return self.call('put', end_point, data=data, **kwargs)

    def patch(self, end_point, data=None, **kwargs):
        return self.call('patch', end_point, data=data, **kwargs)

    def delete(self, end_point, **kwargs):
        return self.call('delete', end_point, **kwargs)

    def get_role(self, role=None):
        default_role = self.config["roles"][self.config["default_role"]]
        return default_role if role is None else self.config["roles"][role]

    def update_credentials(self, credentials):
        self.role = self.get_role(credentials)
        self.auth_strategy.load_config(self, self.role)

    def reset_credentials(self):
        self.role = self.get_role()
        self.auth_strategy.load_config(self, self.role)

    def set_authorization_strategy(self, new_auth_type):
        self.auth_strategy = self.auth_factory.get_auth(new_auth_type)
        self.auth_strategy.load_config(self, self.role)
