# Create a new thread
thread = client.threads.create(project_id="uuid-of-project", user_id="uuid-of-user")
print("Created Thread:", thread)

# Add a message to the thread
message = client.messages.create(
    project_id="uuid-of-project",
    thread_id=thread["thread_id"],
    sender_id="uuid-of-user",
    content="Hello, this is a test message!"
)
print("Created Message:", message)

# Retrieve thread messages
messages = client.messages.list(project_id="uuid-of-project", thread_id=thread["thread_id"])
print("Thread Messages:", messages)
