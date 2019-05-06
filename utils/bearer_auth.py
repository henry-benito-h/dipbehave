from authorization_base import AuthBase


class BearerAuth(AuthBase):
    def __init__(self, request, role_info):
        AuthBase.__init__(self, request, role_info)

    def set_params(self):
        self.request.auth = None
        self.request.headers[self.role_info["token_header"]] = self.role_info["token"]
        return self.request
