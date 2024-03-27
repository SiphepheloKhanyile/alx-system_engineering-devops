#!/usr/bin/python3
"""
Using what i did in the task #0,
extend your Python script to export data in the CSV format.
"""
import requests
import sys

if __name__ == "__main__":
    FILE_NAME = "USER_IC.csv"

    URL = "https://jsonplaceholder.typicode.com/"

    USER = requests.get(URL + f"users/{sys.argv[1]}", timeout=5).json()
    USERNAME = USER.get("name", None)

    TODOS = requests.get(URL + f"users/{sys.argv[1]}/todos", timeout=5).json()

    TITLES_LIST = []
    with open(FILE_NAME, 'w', newline='', encoding='utf-8') as csvfile:

        for DIC in TODOS:
            USER_ID = DIC.get("userId", None)
            TASK_COMPLETED_STATUS = DIC.get("completed", None)
            TASK_TITLE = DIC.get("title", None)

            csvfile.write(
                f'"{USER_ID}","{USERNAME}","{TASK_COMPLETED_STATUS}","{TASK_TITLE}"\
                \n')
