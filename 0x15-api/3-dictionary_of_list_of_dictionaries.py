#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    FILE_NAME = 'todo_all_employees.json'

    USERS = requests.get(URL + "users/", timeout=10).json()

    DICT = {}
    USER_LIST = []
    NEW_DICT = {}

    for user in USERS:
        USER_ID = user.get('id', None)
        USERNAME = user.get('username', None)

        TODOS = requests.get(URL + f"users/{USER_ID}/todos", timeout=10).json()
        USER_LIST = []
        NEW_DICT = {}
        for items in TODOS:
            TASK_TITLE = items.get('title', None)
            TASK_COMP_STATUS = items.get('completed', None)

            NEW_DICT = {
                "username": USERNAME,
                "task": TASK_TITLE,
                "completed": TASK_COMP_STATUS,
            }
            USER_LIST.append(NEW_DICT)

        DICT[f"{USER_ID}"] = USER_LIST

    with open(FILE_NAME, 'w', encoding='utf-8') as json_file:
        json.dump(DICT, json_file)
