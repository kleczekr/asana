import asana
from fuzzywuzzy import fuzz, process
from keys import asana_key, project_gid, crew_info

class AsanaTaskManager:
    def __init__(self, project_gid, asana_key):
        self.project_gid = project_gid
        self.asana_key = asana_key
        self.client = asana.Client.access_token(asana_key)
    def _get_all_tasks(self):
        return self.client.tasks.get_tasks_for_project(self.project_gid, {}, opt_pretty=True)
    def _get_incomplete_tasks(self):
        return self.client.tasks.get_tasks_for_project(self.project_gid, {'completed_since': 'now'}, opt_pretty=True)
    def _get_task_gid(self, task_name):
        tasks = self._get_all_tasks()
        for task in tasks:
            if fuzz.token_sort_ratio(task['name'], task_name) > 90:
                return task['gid']


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
    tasks = client.tasks.get_tasks_for_project(project['gid'], {}, opt_pretty=True)
    # for task in tasks:
    #     print(task)

tasks = client.tasks.get_tasks_for_project(project_gid, {'completed_since': 'now'}, opt_pretty=True)
for task in tasks:
    print(task)
    result = client.tasks.get_task(task['gid'], {}, opt_pretty=True)
    print(result)
    # result = client.tasks.get_dependencies_for_task(task['gid'], {}, opt_pretty=True)
    # print(result)
# Get the list of tasks
# tasks = client.tasks.find_all({'workspace': workspace_gid})

# Print the name of each task
# for task in tasks:
#     print(task['name'])


