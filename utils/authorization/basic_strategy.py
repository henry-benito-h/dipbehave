from authorization.authorization_strategy import AuthorizationStrategy
from requests.auth import HTTPBasicAuth


class BasicStrategy(AuthorizationStrategy):
    """
    This class works with basic authentication and set the headers to work with default value

    Methods
    -------
    set_authentication(request, role)
    set_headers(request, role)
    """

    def set_authentication(self, request, role):
        """
        This method uses Basic authentication to work with request.

        Parameters
        ----------
        request : Request
            The object to work with requests
        role : Dictionary
            This have the information of the role, username and password.
        """
        request.auth = HTTPBasicAuth(role["username"], role["password"])
        return request

    def set_headers(self, request, role):
        """
        This clean the request's headers and set them to default values

        Parameters
        ----------
        request : Request
            The object to work with requests
        role : Dictionary
            This have the information of the role.
        """
        request.headers = request.default_headers
        return request
