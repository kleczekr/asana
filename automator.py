import asana
from keys import asana_key

# Create an Asana client
client = asana.Client.access_token(asana_key)

# retrieve the workspace gid
workspace = client.users.me()['workspaces']
workspace_gid = workspace[0]['gid']

print(workspace_gid)

# Get the list of projects
projects = client.projects.find_all({'workspace': workspace_gid})

# Print the name of each project
for project in projects:
    print(project)

# Get the list of tasks
tasks = client.tasks.find_all({'workspace': workspace_gid})

# Print the name of each task
for task in tasks:
    print(task['name'])


