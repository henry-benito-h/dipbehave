from authorization_base import AuthBase
from requests.auth import HTTPBasicAuth


class BasicAuth(AuthBase):
    def __init__(self, request, role_info):
        AuthBase.__init__(request, role_info)

    def set_params(self):
        self.request.auth = HTTPBasicAuth(self.role_info["username"], self.role_info["password"])
        return self.request
