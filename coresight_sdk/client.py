"""
client.py: Main client for interacting with the Multi-Tenant Messaging API via the Coresight SDK.
"""

import requests
from typing import Optional, Dict, Any, List, Union
from .exceptions import ApiException


class CoresightClient:
    """
    Python SDK client for the Multi-Tenant Messaging API.
    """

    def __init__(self, base_url: str, api_key: Optional[str] = None) -> None:
        """
        :param base_url: Base URL of the deployed Multi-Tenant Messaging API.
        :param api_key:  Optional API key (required for endpoints protected by ApiKeyAuth).
        """
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key

    def _get_headers(self) -> Dict[str, str]:
        """
        Prepare headers for all HTTP requests, including content type and optional x-api-key.
        """
        headers = {
            "Content-Type": "application/json"
        }
        if self.api_key:
            headers["x-api-key"] = self.api_key
        return headers

    def _handle_response(self, response: requests.Response) -> Union[Dict[str, Any], List[Any], str]:
        """
        Parse HTTP response, raise ApiException if not 2xx, otherwise return JSON or text.
        """
        if not response.ok:
            try:
                details = response.json()
            except Exception:
                details = {}
            raise ApiException(
                status_code=response.status_code,
                message=response.text,
                details=details
            )

        # Try returning JSON, fallback to text if parsing fails.
        try:
            return response.json()
        except ValueError:
            return response.text

    # -------------------------------------------------------------------------
    # 1. SignUp (POST /signup)
    # -------------------------------------------------------------------------
    def sign_up(self, name: str, email: str, password: str, package: str) -> Dict[str, Any]:
        """
        Register a new client and generate an API key.

        :param name: Client's name
        :param email: Client's email
        :param password: Password
        :param package: Plan package (Free, Basic, Premium)
        :return: Dictionary with client_id, api_key, message
        """
        url = f"{self.base_url}/signup"
        payload = {
            "name": name,
            "email": email,
            "password": password,
            "package": package
        }
        resp = requests.post(url, json=payload, headers=self._get_headers())
        return self._handle_response(resp)

    # -------------------------------------------------------------------------
    # 2. Login (POST /login)
    # -------------------------------------------------------------------------
    def login(self, email: str, password: str) -> Dict[str, Any]:
        """
        Authenticate a client and receive a token.

        :param email: Client's email
        :param password: Client's password
        :return: Dictionary with "token"
        """
        url = f"{self.base_url}/login"
        payload = {
            "email": email,
            "password": password
        }
        resp = requests.post(url, json=payload, headers=self._get_headers())
        return self._handle_response(resp)

    # -------------------------------------------------------------------------
    # 3. Clients Module
    # -------------------------------------------------------------------------
    def create_client(self, name: str, email: str, password: str, package: str) -> Dict[str, Any]:
        """
        Create a new client (requires API key).

        :return: Dictionary with client_id, api_key, message
        """
        url = f"{self.base_url}/clients"
        payload = {
            "name": name,
            "email": email,
            "password": password,
            "package": package
        }
        resp = requests.post(url, json=payload, headers=self._get_headers())
        return self._handle_response(resp)

    def get_client(self, client_id: int) -> Dict[str, Any]:
        """
        Retrieve client details (requires API key).

        :return: Dictionary with client details
        """
        url = f"{self.base_url}/clients/{client_id}"
        resp = requests.get(url, headers=self._get_headers())
        return self._handle_response(resp)

    def update_client(self, client_id: int, name: str, email: str, package: str) -> Dict[str, Any]:
        """
        Update client details (requires API key).

        :return: Dictionary with "message"
        """
        url = f"{self.base_url}/clients/{client_id}"
        payload = {
            "name": name,
            "email": email,
            "package": package
        }
        resp = requests.put(url, json=payload, headers=self._get_headers())
        return self._handle_response(resp)

    # -------------------------------------------------------------------------
    # 4. Users Module
    # -------------------------------------------------------------------------
    def create_anonymous_user(self, client_id: int, session_id: str) -> Dict[str, Any]:
        """
        Create a new anonymous user for a given client (requires API key).

        :return: Dictionary with user_id, session_id, message
        """
        url = f"{self.base_url}/clients/{client_id}/anonymous-users"
        payload = {
            "session_id": session_id
        }
        resp = requests.post(url, json=payload, headers=self._get_headers())
        return self._handle_response(resp)

    def get_anonymous_user(self, client_id: int, user_id: int) -> Dict[str, Any]:
        """
        Get details of an anonymous user by ID (requires API key).

        :return: Dictionary with user details
        """
        url = f"{self.base_url}/clients/{client_id}/anonymous-users/{user_id}"
        resp = requests.get(url, headers=self._get_headers())
        return self._handle_response(resp)

    def create_authenticated_user(self, client_id: int, email: str, name: str) -> Dict[str, Any]:
        """
        Create an authenticated user for a client (requires API key).

        :return: Dictionary with user_id, email, name, message
        """
        url = f"{self.base_url}/clients/{client_id}/authenticated-users"
        payload = {
            "email": email,
            "name": name
        }
        resp = requests.post(url, json=payload, headers=self._get_headers())
        return self._handle_response(resp)

    def get_authenticated_user(self, client_id: int, user_id: int) -> Dict[str, Any]:
        """
        Get details of an authenticated user by ID (requires API key).

        :return: Dictionary with user details
        """
        url = f"{self.base_url}/clients/{client_id}/authenticated-users/{user_id}"
        resp = requests.get(url, headers=self._get_headers())
        return self._handle_response(resp)

    def list_users(self, client_id: int) -> List[Dict[str, Any]]:
        """
        List all users (anonymous & authenticated) for a client (requires API key).

        :return: List of user dictionaries
        """
        url = f"{self.base_url}/clients/{client_id}/users"
        resp = requests.get(url, headers=self._get_headers())
        return self._handle_response(resp)

    # -------------------------------------------------------------------------
    # 5. Threads Module
    # -------------------------------------------------------------------------
    def create_thread(self, client_id: int) -> Dict[str, Any]:
        """
        Create a new thread for a given client (requires API key).

        :return: Dictionary with thread_id, message
        """
        url = f"{self.base_url}/clients/{client_id}/threads"
        resp = requests.post(url, headers=self._get_headers())
        return self._handle_response(resp)

    def get_thread(self, client_id: int, thread_id: int) -> Dict[str, Any]:
        """
        Get details of a thread (requires API key).

        :return: Dictionary with thread details
        """
        url = f"{self.base_url}/clients/{client_id}/threads/{thread_id}"
        resp = requests.get(url, headers=self._get_headers())
        return self._handle_response(resp)

    # -------------------------------------------------------------------------
    # 6. Messages Module
    # -------------------------------------------------------------------------
    def create_message(self, client_id: int, thread_id: int, user_input: str) -> Dict[str, Any]:
        """
        Create a new message in a thread (requires API key).

        :return: Dictionary with message_id, thread_id, user_input, llm_response, created_at
        """
        url = f"{self.base_url}/clients/{client_id}/threads/{thread_id}/messages"
        payload = {
            "user_input": user_input
        }
        resp = requests.post(url, json=payload, headers=self._get_headers())
        return self._handle_response(resp)

    def get_message(self, client_id: int, message_id: int) -> Dict[str, Any]:
        """
        Get details of a specific message by ID (requires API key).

        :return: Dictionary with message details
        """
        url = f"{self.base_url}/clients/{client_id}/messages/{message_id}"
        resp = requests.get(url, headers=self._get_headers())
        return self._handle_response(resp)

    def get_thread_messages(self, client_id: int, thread_id: int) -> List[Dict[str, Any]]:
        """
        Retrieve message history of a thread (requires API key).

        :return: List of message dictionaries
        """
        url = f"{self.base_url}/clients/{client_id}/threads/{thread_id}/messages"
        resp = requests.get(url, headers=self._get_headers())
        return self._handle_response(resp)

    # -------------------------------------------------------------------------
    # 7. Feedback Module
    # -------------------------------------------------------------------------
    def add_feedback(self, client_id: int, message_id: int, feedback: str) -> Dict[str, Any]:
        """
        Add feedback to a message (requires API key).

        :return: Dictionary with feedback_id, message_id, feedback, created_at
        """
        url = f"{self.base_url}/clients/{client_id}/messages/{message_id}/feedback"
        payload = {
            "feedback": feedback
        }
        resp = requests.post(url, json=payload, headers=self._get_headers())
        return self._handle_response(resp)

    def get_feedback(self, client_id: int, feedback_id: int) -> Dict[str, Any]:
        """
        Retrieve a specific feedback entry (requires API key).

        :return: Dictionary with feedback details
        """
        url = f"{self.base_url}/clients/{client_id}/feedback/{feedback_id}"
        resp = requests.get(url, headers=self._get_headers())
        return self._handle_response(resp)

    # -------------------------------------------------------------------------
    # 8. LLM Chat Completion
    # -------------------------------------------------------------------------
    def chat_with_llm(
        self,
        client_id: int,
        user_input: str,
        thread_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Send a prompt to the LLM and receive a response (requires API key).

        :param client_id: The client ID
        :param user_input: Prompt to send to the LLM
        :param thread_id: (Optional) Existing thread ID to associate the chat
        :return: Dictionary with thread_id and response
        """
        url = f"{self.base_url}/clients/{client_id}/llm/chat"
        payload: Dict[str, Any] = {"user_input": user_input}
        if thread_id is not None:
            payload["thread_id"] = thread_id

        resp = requests.post(url, json=payload, headers=self._get_headers())
        return self._handle_response(resp)

    # -------------------------------------------------------------------------
    # 9. Subscription Management
    # -------------------------------------------------------------------------
    def create_subscription(self, client_id: int, price_id: str, plan: str) -> Dict[str, Any]:
        """
        Create a subscription for a client (requires API key).

        :return: Dictionary with subscription_id, message
        """
        url = f"{self.base_url}/clients/{client_id}/subscriptions"
        payload = {
            "price_id": price_id,
            "plan": plan
        }
        resp = requests.post(url, json=payload, headers=self._get_headers())
        return self._handle_response(resp)

    def update_subscription(
        self,
        client_id: int,
        subscription_id: str,
        new_price_id: str,
        new_plan: str
    ) -> Dict[str, Any]:
        """
        Update an existing subscription for a client (requires API key).

        :return: Dictionary with subscription_id, message
        """
        url = f"{self.base_url}/clients/{client_id}/subscriptions/{subscription_id}"
        payload = {
            "new_price_id": new_price_id,
            "new_plan": new_plan
        }
        resp = requests.put(url, json=payload, headers=self._get_headers())
        return self._handle_response(resp)

    def cancel_subscription(self, client_id: int, subscription_id: str) -> Dict[str, Any]:
        """
        Cancel a subscription for a client (requires API key).

        :return: Dictionary with subscription_id, message
        """
        url = f"{self.base_url}/clients/{client_id}/subscriptions/{subscription_id}"
        resp = requests.delete(url, headers=self._get_headers())
        return self._handle_response(resp)
