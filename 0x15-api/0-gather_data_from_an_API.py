#!/usr/bin/python3
"""
Uses `jsonplaceholder` API to retrieve employee to-do's
Using employee ID passed to script
"""
import sys
import requests


if __name__ == "__main__":
    # https://jsonplaceholder.typicode.com/users/1/todos
    Url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(Url + f"users/{sys.argv[1]}", timeout=5).json()
    username = user.get("name", None)

    todos = requests.get(Url + f"users/{sys.argv[1]}/todos", timeout=5).json()
    # todos_list = json.dumps(todos, indent=2)

    complete = 0
    tasks = 0
    TASK_TITLE = []

    for dic in todos:
        tasks = tasks + 1
        if dic.get("completed", None) is True:
            complete = complete + 1
            TASK_TITLE.append(dic.get("title"))

    print(
        f"Employee {username} is done with tasks({complete}/{tasks}):")
    for title in TASK_TITLE:
        print(f"\t{title}")
