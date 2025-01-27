# Add feedback to a message
feedback = client.feedback.add(
    project_id="uuid-of-project",
    message_id="uuid-of-message",
    user_id="uuid-of-user",
    rating=5,
    comment="Great response!"
)
print("Feedback:", feedback)

# List feedback for a message
feedback_list = client.feedback.list(project_id="uuid-of-project", message_id="uuid-of-message")
print("Feedback List:", feedback_list)
