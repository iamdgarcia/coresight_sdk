class Feedback:
    def __init__(self, request_handler):
        self.request_handler = request_handler

    def add(self, project_id: str, message_id: str, user_id: str, rating: int, comment: str = "") -> dict:
        """
        Add feedback for a message.
        """
        payload = {"user_id": user_id, "rating": rating, "comment": comment}
        return self.request_handler.post(f"/projects/{project_id}/messages/{message_id}/feedback", payload)

    def list(self, project_id: str, message_id: str) -> list:
        """
        List all feedback for a message.
        """
        return self.request_handler.get(f"/projects/{project_id}/messages/{message_id}/feedback")
