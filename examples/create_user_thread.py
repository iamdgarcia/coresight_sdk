from coresight_sdk.client import CoresightClient

# 1. Initialize the SDK client
client = CoresightClient(
    base_url="https://myapi.execute-api.myregion.amazonaws.com/Prod",
    api_key="YOUR_API_KEY"  # Optional but required for endpoints needing x-api-key
)

# 2. Sign up a new client
signup_response = client.sign_up(
    name="John Doe",
    email="[email protected]",
    password="Secret123",
    package="Free"  # one of "Free", "Basic", or "Premium"
)
print("Sign-up response:", signup_response)

# 3. Log in an existing client
login_response = client.login(
    email="[email protected]",
    password="Secret123"
)
print("Login token:", login_response.get("token"))

# 4. Create a new thread (requires valid x-api-key)
thread_response = client.create_thread(client_id=signup_response["client_id"])
print("New thread:", thread_response)

# 5. Create a message in the thread
message_response = client.create_message(
    client_id=signup_response["client_id"],
    thread_id=thread_response["thread_id"],
    user_input="Hello, I'd like some help with an issue."
)
print("Message created:", message_response)
