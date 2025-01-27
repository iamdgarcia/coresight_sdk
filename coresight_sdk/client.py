from coresight_sdk.projects import Projects
from coresight_sdk.users import Users
from coresight_sdk.threads import Threads
from coresight_sdk.messages import Messages
from coresight_sdk.feedback import Feedback
from coresight_sdk.subscriptions import Subscriptions
from coresight_sdk.utils import APIRequestHandler


class CoresightClient:
    def __init__(self, base_url: str, api_key: str) -> None:
        """
        Initialize the Coresight SDK client.
        :param base_url: Base URL of the deployed Multi-Tenant Messaging API.
        :param api_key: API key for accessing project-specific resources.
        """
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.request_handler = APIRequestHandler(self.base_url, self.api_key)

        # Initialize modules
        self.projects = Projects(self.request_handler)
        self.users = Users(self.request_handler)
        self.threads = Threads(self.request_handler)
        self.messages = Messages(self.request_handler)
        self.feedback = Feedback(self.request_handler)
        self.subscriptions = Subscriptions(self.request_handler)
    def health_check(self) -> dict:
        """
        Test the API connection with a health check endpoint.
        """
        return self.request_handler.get("/health")