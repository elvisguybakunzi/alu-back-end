#!/usr/bin/python3
"""
Exports employee tasks to a JSON file based on employee ID.
"""

import json
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
    filename = "{}.json".format(employee_id)

    data = {employee_id: []}

    for task in response_todos:
        data[employee_id].append({"task": task.get('title'), "completed": task.get('completed'), "username": employee_name})

    with open(filename, 'w') as file:
        json.dump(data, file)
