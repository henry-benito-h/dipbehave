import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from authorization.basic_auth import BasicAuth
from authorization.bearer_auth import BearerAuth


class AuthFactory:
    def __init__(self):
        self.auth_type = {
            'basic': BasicAuth,
            'bearer': BearerAuth
        }

    def get_auth(self, auth_type):
        return self.auth_type[auth_type]
