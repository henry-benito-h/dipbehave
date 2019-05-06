class AuthBase:
    def __init__(self, request, role_info):
        self.request = request
        self.role_info = role_info

    def set_params(self):
        pass
