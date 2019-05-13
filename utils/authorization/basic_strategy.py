from authorization.authorization_strategy import AuthorizationStrategy
from requests.auth import HTTPBasicAuth


class BasicStrategy(AuthorizationStrategy):
    def set_authentication(self, request, role):
        request.auth = HTTPBasicAuth(role["username"], role["password"])
        return request

    def set_headers(self, request, role):
        request.headers = request.default_headers
        return request
