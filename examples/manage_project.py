from sdk.client import CoresightClient

# Initialize the SDK
client = CoresightClient(base_url="https://api.example.com", api_key="project-specific-api-key")

# Create a new project
project = client.projects.create(name="New Project", llm_config={"model": "gpt-4", "temperature": 0.7})
print("Created Project:", project)

# Retrieve a specific project
project_details = client.projects.get(project_id="uuid-of-project")
print("Project Details:", project_details)

# List all projects
all_projects = client.projects.list()
print("All Projects:", all_projects)
