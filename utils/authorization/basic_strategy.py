from authorization.authorization_base import AuthBase
from requests.auth import HTTPBasicAuth


class BasicAuth(AuthBase):
    def __init__(self, request, role_info):
        AuthBase.__init__(self, request, role_info)

    def set_params(self):
        try:
            self.request.auth = HTTPBasicAuth(self.role_info["username"], self.role_info["password"])
            if "token_header" in self.role_info:
                if self.role_info["token_header"] in self.request.headers:
                    del self.request.headers[self.role_info["token_header"]]
            return self.request
        except KeyError:
            return None
