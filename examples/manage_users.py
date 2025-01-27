# Add an anonymous user
anonymous_user = client.users.create_anonymous(project_id="uuid-of-project", session_id="session-123")
print("Anonymous User:", anonymous_user)

# Add an authenticated user
authenticated_user = client.users.create_authenticated(
    project_id="uuid-of-project",
    email="user@example.com",
    name="John Doe",
    metadata={"role": "admin"}
)
print("Authenticated User:", authenticated_user)

# List users in a project
users = client.users.list(project_id="uuid-of-project")
print("Users in Project:", users)
