#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"

    USER = requests.get(URL + f"users/{sys.argv[1]}", timeout=5).json()
    USERNAME = USER.get("username", None)
    USER_ID = USER.get("id", None)
    FILE_NAME = f"{USER_ID}.json"

    TODOS = requests.get(URL + f"users/{sys.argv[1]}/todos", timeout=5).json()

    DICT_LIST = []

    for items in TODOS:
        TASK_TITLE = items.get("title")
        TASK_COMP_STATUS = items.get("completed")

        NEW_DICT = {
            "task": TASK_TITLE,
            "completed": TASK_COMP_STATUS,
            "username": USERNAME
        }

        DICT_LIST.append(NEW_DICT)

    DICT = {f"{USER_ID}": DICT_LIST}

    with open(FILE_NAME, 'w', encoding='utf-8') as JSON_FILE:
        json.dump(DICT, JSON_FILE)
