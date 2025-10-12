import requests


class PhonnoClient:
    """
    A generic fetch client for Phonno that automatically adds Authorization header.
    API interface mimics Node.js fetch.

    Usage:
        client = PhonnoClient(
            origin="...",
            project_name="...",  # deprecated, kept for backward compatibility
            app_name="legacy",
            token="your_token_here"
        )

        # GET request
        response = client.get("/api/v2/{app_name}/similar")

        # POST request
        response = client.post("/api/v2/{app_name}/chat", json={"key": "value"})
    """

    def __init__(self, origin, project_name=None, app_name=None, token=""):
        """
        Initialize the Phonno client.

        Args:
            origin (str): The base URL
            project_name (str): Deprecated parameter, kept for backward compatibility
            app_name (str): The application name (e.g., "legacy")
            token (str): The authentication token
        """
        self.origin = origin.rstrip("/")

        # Handle deprecated project_name parameter
        if project_name and not app_name:
            app_name = project_name

        self.app_name = app_name
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
        Replaces {app_name} placeholder if present.

        Args:
            pathname (str): The path (e.g., "/api/v2/{app_name}/similar")

        Returns:
            str: Complete URL
        """
        # Replace {app_name} placeholder
        pathname = pathname.replace("{app_name}", self.app_name)

        # Ensure pathname starts with /
        if not pathname.startswith("/"):
            pathname = "/" + pathname

        return self.origin + pathname

    def get(self, pathname, headers=None, params=None):
        """
        Perform a GET request.

        Args:
            pathname (str): The path (e.g., "/api/v2/{app_name}/similar")
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
            pathname (str): The path (e.g., "/api/v2/{app_name}/chat")
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
