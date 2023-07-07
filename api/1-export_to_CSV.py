#!/usr/bin/python3
"""
Exports employee tasks to a CSV file based on employee ID.
"""

import csv
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
    filename = "{}.csv".format(employee_id)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in response_todos:
            writer.writerow([employee_id, employee_name, task.get('completed'), task.get('title')])

