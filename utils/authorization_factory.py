import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from basic_auth import BasicAuth
from bearer_auth import BearerAuth
from requests_oauthlib import OAuth1


class AuthFactory:
    def __init__(self):
        self.auth_type = {
            'basic': BasicAuth,
            'bearer': BearerAuth
        }

    def get_auth(self, auth_type):
        return self.auth_type[auth_type]
