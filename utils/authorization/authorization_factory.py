import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from authorization.basic_strategy import BasicStrategy
from authorization.bearer_strategy import BearerStrategy


class AuthFactory:
    """
    This class is a factory to work with authorization strategies
    """
    def __init__(self):
        self.auth_type = {
            'basic': BasicStrategy,
            'bearer': BearerStrategy
        }

    def get_auth(self, auth_type):
        """
        This method allows to recover an authorization strategy given an string
        :param auth_type: A string value that identifies a strategy name
        :return: Strategy object for authorization
        """
        return self.auth_type[auth_type]
