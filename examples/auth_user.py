from coresight_sdk.client import ProjectClient

# Initialize the SDK with a project-specific API key
client = ProjectClient(api_key="y3PJiz4pjXGGxnGq8e8p9nueefiysp15aoumkW95",base_api_url="https://ku7dfi9gaj.execute-api.eu-west-3.amazonaws.com/Prod/")

# Get registered user
current_user = client.users.get("test@gmail.com")[0]

# Create it otherwise
# current_user = client.users.create_authenticated(email="test@gmail.com",name="John Doe")
print("Auth User User:", current_user)

# Create a thread
thread = client.threads.create(user_id=current_user['user_id'])
print("Thread Created:", thread)

# # Create a thread
# threads = client.threads.list(user_id=current_user['user_id'])
# print("Active threads", threads)

thread = threads[0]

messages = client.messages.list(user_id=current_user['user_id'],thread_id=thread["thread_id"])
print(messages)
# Add a message to the thread
message = client.messages.create(user_id=current_user['user_id'],thread_id=thread["thread_id"], sender_id="uuid-of-user", content="Hello, world!")
print("Message Sent:", message)
