from authorization.authorization_strategy import AuthorizationStrategy


class BearerStrategy(AuthorizationStrategy):
    """
    This class works with bearer authorization avoiding authentication
     and setting headers information according the role.

    Methods
    -------
    set_authentication(request, role)
    set_headers(request, role)
    """
    def set_authentication(self, request, role):
        """
        This method sets to None the authentication for request.

        Parameters
        ----------
        request : Request
            The object to work with requests
        role : Dictionary
            This have the information of the role, username and password.
        """
        request.auth = None
        return request

    def set_headers(self, request, role):
        """
        This clean the request's headers and set them the role's values.

        Parameters
        ----------
        request : Request
            The object to work with requests
        role : Dictionary
            This have the information of the role.
        """
        request.headers = request.default_headers
        for header in role["headers"]:
            request.headers[header] = role["headers"][header]
        return request
