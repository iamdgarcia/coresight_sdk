class Threads:
    def __init__(self, request_handler):
        self.request_handler = request_handler

    def create(self, project_id: str, user_id: str) -> dict:
        """
        Create a new thread in a project.
        """
        payload = {"user_id": user_id}
        return self.request_handler.post(f"/projects/{project_id}/threads", payload)

    def get(self, project_id: str, thread_id: str) -> dict:
        """
        Retrieve details of a specific thread.
        """
        return self.request_handler.get(f"/projects/{project_id}/threads/{thread_id}")

    def list(self, project_id: str) -> list:
        """
        List all threads in a project.
        """
        return self.request_handler.get(f"/projects/{project_id}/threads")
