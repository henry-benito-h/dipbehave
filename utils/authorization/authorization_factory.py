import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from authorization.basic_strategy import BasicStrategy
from authorization.bearer_strategy import BearerStrategy


class AuthFactory:
    def __init__(self):
        self.auth_type = {
            'basic': BasicStrategy,
            'bearer': BearerStrategy
        }

    def get_auth(self, auth_type):
        return self.auth_type[auth_type]
