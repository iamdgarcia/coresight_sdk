class Messages:
    def __init__(self, request_handler):
        self.request_handler = request_handler

    def create(self, project_id: str, thread_id: str, sender_id: str, content: str) -> dict:
        """
        Create a new message in a thread.
        """
        payload = {"sender_id": sender_id, "content": content}
        return self.request_handler.post(f"/projects/{project_id}/threads/{thread_id}/messages", payload)

    def list(self, project_id: str, thread_id: str) -> list:
        """
        Retrieve all messages in a thread.
        """
        return self.request_handler.get(f"/projects/{project_id}/threads/{thread_id}/messages")
