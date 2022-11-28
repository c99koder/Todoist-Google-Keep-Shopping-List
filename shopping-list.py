#!/usr/bin/python3

#  Copyright (C) 2022 Sam Steele
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import sys, keyring, gkeepapi
from todoist_api_python.api import TodoistAPI

TODOIST_ACCESS_TOKEN = '' #At the bottom of Settings > Integrations in the web/desktop app
TODOIST_PROJECT_ID = '' #Copy from URL bar https://todoist.com/app/project/<project ID>
GOOGLE_USERNAME = ''
GOOGLE_PASSWORD = '' #Create an app password at https://myaccount.google.com/apppasswords
REMOVE_FROM_KEEP = True #Remove items from Google Keep after transferring to Todoist

keep = gkeepapi.Keep()
todoist = TodoistAPI(TODOIST_ACCESS_TOKEN)
tasks = todoist.get_tasks(project_id=TODOIST_PROJECT_ID)

def exists(content):
	for task in tasks:
		if task.content.lower() == content.lower():
			print(f"Already exists in Todoist: {task.content} ({str(task.id)})")
			return True
	return False

token = keyring.get_password('google-keep-token', GOOGLE_USERNAME)
if token is None:
	keep.login(GOOGLE_USERNAME, GOOGLE_PASSWORD)
else:
	keep.resume(GOOGLE_USERNAME, token)

keyring.set_password('google-keep-token', GOOGLE_USERNAME, keep.getMasterToken())
shopping_list = list(keep.find(query='Google Assistant shopping list'))
if len(shopping_list) == 0:
	print("Unable to find Google Assistant shopping list")
	sys.exit(1)
else:
	shopping_list = shopping_list[0]

print(f"Shopping list note ID: {shopping_list.id}")

for item in shopping_list.items:
	if item.checked != True:
		if not exists(item.text):
			t = todoist.add_task(content=item.text, project_id=TODOIST_PROJECT_ID)
			print(f"Created task: {item.text} ({t.id})")

	if REMOVE_FROM_KEEP:
		print(f"Removing item from Google Keep: {item.id}")
		item.delete()

keep.sync()
