#!/usr/bin/python3
"""Gathering data from API placeholder"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(argv[1]))

    name_obj = response.json()

    emp_name = name_obj.get('name')

    usrid = name_obj.get('id')

    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks_items = []
    tasks_obj = response.json()

    completed = 0
    tasks = 0

    for task in tasks_obj:
        if task.get('userId') == usrid:
            task += 1
            if task.get('completed'):
                completed += 1
                tasks_items.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(emp_name, completed, tasks))

    for t in tasks_items:
        print('\t', t)
