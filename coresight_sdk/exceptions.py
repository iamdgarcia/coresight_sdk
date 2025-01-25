"""
exceptions.py: Contains custom exceptions for the Coresight SDK.
"""

from typing import Optional, Dict


class ApiException(Exception):
    """
    Exception for non-2xx responses from the Multi-Tenant Messaging API.
    """

    def __init__(
        self,
        status_code: int,
        message: str = "",
        details: Optional[Dict] = None
    ) -> None:
        """
        :param status_code: HTTP status code from the response
        :param message: Error message (usually response.text)
        :param details: Parsed JSON body from the error (if any)
        """
        super().__init__(f"API Error {status_code}: {message}")
        self.status_code = status_code
        self.message = message
        self.details = details or {}
