#!/usr/bin/python3
""" Export to JSON """
import json
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(argv[1]))

    name_obj = response.json()

    emp_name = name_obj.get('username')

    usrid = name_obj.get('id')

    completed = []

    response = requests.get('https://jsonplaceholder.typicode.com/todos')

    tasks_obj = response.json()

    tasks_items = []

    for task in tasks_obj:
        if task.get('userId') == usrid:
            completed.append(task.get('completed'))
            tasks_items.append(task.get('title'))
    for i, e in enumerate(tasks_items):
        l = [{'username': emp_name, 'completed': completed[i], 'task': e}]
    json_dict = {usrid: l}
    with open('{}.json'.format(argv[1]), mode='w') as json_file:
        json.dump({usrid: l}, json_file)
