#!/usr/bin/python3
"""
Exports tasks of all employees to a JSON file.
"""

import json
import requests


if __name__ == "__main__":
    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    response_users = requests.get(url_users).json()
    response_todos = requests.get(url_todos).json()

    data = {}

    for user in response_users:
        employee_id = user.get('id')
        employee_name = user.get('name')
        employee_todos = [task for task in response_todos if task.get('userId') == employee_id]

        data[employee_id] = []
        for task in employee_todos:
            data[employee_id].append({"task": task.get('title'), "completed": task.get('completed'), "username": employee_name})

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
