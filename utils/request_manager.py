import sys
import os
import requests

sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from authorization.authorization_factory import AuthFactory


class Request:
    """Class client for api service"""
    def __init__(self, config):
        self.config = config
        self.config_headers = config["headers"]
        self.base_url = f'{config["host"]}{config["root_path"]}'
        self.headers = {
            'Content-Type': f'{self.config_headers["Content-Type"]}'
        }
        self.auth_factory = AuthFactory()
        self.auth_type = self.auth_factory.get_auth(config["auth"])(self, self.config["roles"]["admin"])
        self.auth_type.set_params()

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

    def update_credentials(self, credentials):
        # self.auth = OAuth1(self.config[credentials]['consumer_key'], self.config[credentials]['consumer_secret'])
        self.headers['X-TrackerToken'] = f'{self.config["roles"][credentials]}';

    def reset_credentials(self):
        self.headers['X-TrackerToken'] = None;
