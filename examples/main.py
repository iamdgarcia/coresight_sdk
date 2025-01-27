from coresight_sdk.client import ProjectClient

# Initialize the SDK with a project-specific API key
client = ProjectClient(api_key="your-api-key")

# Check the health of the API
# print(client.health_check())

# Add an anonymous user
response = client.users.create_anonymous(session_id="session123")
print("Anonymous User:", response)

# Create a thread
thread = client.threads.create(user_id=response['user_id'])
print("Thread Created:", thread)



# Add a message to the thread
message = client.messages.create(user_id=response['user_id'],thread_id=thread["thread_id"], sender_id="uuid-of-user", content="Hello, world!")
print("Message Sent:", message)
