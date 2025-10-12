import requests


class PhonnoClient:
    """
    A generic fetch client for Phonno that automatically adds Authorization header.
    API interface mimics Node.js fetch.

    Usage:
        client = PhonnoClient(
            origin="...",
            token="your_token_here"
        )

        # GET request
        response = client.get("/api/v2/example/similar")

        # POST request
        response = client.post("/api/v2/example/chat", json={"key": "value"})
    """

    def __init__(self, origin, token=""):
        """
        Initialize the Phonno client.

        Args:
            origin (str): The base URL
            token (str): The authentication token
        """
        self.origin = origin.rstrip("/")
        self.token = token

    def _get_headers(self, extra_headers=None):
        """
        Get default headers with Authorization token.

        Args:
            extra_headers (dict): Additional headers to merge

        Returns:
            dict: Complete headers dictionary
        """
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Bearer " + self.token,
        }
        if extra_headers:
            headers.update(extra_headers)
        return headers

    def _build_url(self, pathname):
        """
        Build full URL from pathname.

        Args:
            pathname (str): The path

        Returns:
            str: Complete URL
        """
        # Ensure pathname starts with /
        if not pathname.startswith("/"):
            pathname = "/" + pathname

        return self.origin + pathname

    def get(self, pathname, headers=None, params=None):
        """
        Perform a GET request.

        Args:
            pathname (str): The path
            headers (dict): Additional headers (optional)
            params (dict): URL query parameters (optional)

        Returns:
            requests.Response: The response object
        """
        url = self._build_url(pathname)
        headers = self._get_headers(headers)
        response = requests.get(url, headers=headers, params=params)
        return response

    def post(self, pathname, json=None, data=None, headers=None):
        """
        Perform a POST request.

        Args:
            pathname (str): The path
            json (dict): JSON payload (optional)
            data (dict): Form data payload (optional)
            headers (dict): Additional headers (optional)

        Returns:
            requests.Response: The response object
        """
        url = self._build_url(pathname)
        headers = self._get_headers(headers)
        response = requests.post(url, json=json, data=data, headers=headers)
        return response
