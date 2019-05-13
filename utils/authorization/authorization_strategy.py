class AuthorizationStrategy:
    def set_authentication(self, request, role):
        pass

    def set_headers(self, request, role):
        pass

    def load_config(self, request, role):
        try:
            self.set_authentication(request, role)
            self.set_headers(request, role)
        except KeyError:
            return None
