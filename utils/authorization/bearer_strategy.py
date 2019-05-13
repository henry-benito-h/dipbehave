from authorization.authorization_strategy import AuthorizationStrategy


class BearerStrategy(AuthorizationStrategy):
    def set_authentication(self, request, role):
        request.auth = None
        return request

    def set_headers(self, request, role):
        for header in role["headers"]:
            request.headers[header] = role["headers"][header]
        return request
