from coresight_sdk.users import Users
from coresight_sdk.threads import Threads
from coresight_sdk.messages import Messages
from coresight_sdk.feedback import Feedback
from coresight_sdk.utils import APIRequestHandler

BASE_API_URL = "https://10j5fuhfua.execute-api.eu-west-3.amazonaws.com/Prod/"

class ProjectClient:
    def __init__(self, api_key: str) -> None:
        """
        Initialize the SDK for a specific project.

        :param api_key: API key associated with the project.
        """
        self.api_key = api_key
        self.request_handler = APIRequestHandler(BASE_API_URL, self.api_key)
        self.project_id = self.get_from_key()['project_id']
        # Initialize project-scoped modules
        self.users = Users(self.request_handler,self.project_id)
        self.threads = Threads(self.request_handler,self.project_id)
        self.messages = Messages(self.request_handler,self.project_id)
        self.feedback = Feedback(self.request_handler,self.project_id)

    def health_check(self) -> dict:
        """
        Test the API connection with a health check endpoint.
        """
        return self.request_handler.get("/health")

    def get_from_key(self) -> dict:
        """
        Retrieve details of a specific project.
        """
        return self.request_handler.get(f"/projects/from_api_key")