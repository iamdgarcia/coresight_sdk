class Users:
    def __init__(self, request_handler):
        self.request_handler = request_handler

    def create_anonymous(self, project_id: str, session_id: str) -> dict:
        """
        Create an anonymous user for a project.
        """
        payload = {"session_id": session_id}
        return self.request_handler.post(f"/projects/{project_id}/anonymous-users", payload)

    def create_authenticated(self, project_id: str, email: str, name: str, metadata: dict = None) -> dict:
        """
        Create an authenticated user for a project.
        """
        payload = {"email": email, "name": name, "metadata": metadata or {}}
        return self.request_handler.post(f"/projects/{project_id}/authenticated-users", payload)

    def list(self, project_id: str) -> list:
        """
        List all users in a project.
        """
        return self.request_handler.get(f"/projects/{project_id}/users")
