#!/usr/bin/python3
"""
Uses `jsonplaceholder` API to retrieve employee to-do's
Using employee ID passed to script
"""
import requests
import sys


if __name__ == "__main__":
    # https://jsonplaceholder.typicode.com/users/1/todos
    URL = "https://jsonplaceholder.typicode.com/"

    USER = requests.get(URL + f"users/{sys.argv[1]}", timeout=5).json()
    USERNAME = USER.get("name", None)

    TODOS = requests.get(URL + f"users/{sys.argv[1]}/todos", timeout=5).json()

    COMPLETED = 0
    TASKS = 0
    TASK_TITLE = []

    for dic in TODOS:
        TASKS = TASKS + 1
        if dic.get("completed", None) is True:
            COMPLETED = COMPLETED + 1
            TASK_TITLE.append(dic.get("title"))

    print(
        f"Employee {USERNAME} is done with tasks({COMPLETED}/{TASKS}):")
    for title in TASK_TITLE:
        print(f"\t {title}")
