#!/usr/bin/python3
"""
Gathers data from an API based on employee ID.
"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        exit()

    employee_id = argv[1]

    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)

    response_user = requests.get(url_user).json()
    response_todos = requests.get(url_todos).json()

    employee_name = response_user.get('name')
    todos_completed = [task for task in response_todos if task.get('completed')]
    total_tasks = len(response_todos)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(todos_completed), total_tasks))
    for task in todos_completed:
        print("\t{}".format(task.get('title')))

