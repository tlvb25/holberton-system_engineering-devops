#!/usr/bin/python3
from sys import argv
import requests

if __name__ == "__main__":
    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(argv[1]))

    name_obj = response.json()

    emp_name = name_obj.get('name')

    usrid = name_obj.get('id')

    tasks = 0
    completed = 0

    response = requests.get('https://jsonplaceholder.typicode.com/todos')

    tasks_obj = response.json()

    tasks_items = []

    for task in tasks_obj:
        if task.get('userId') == usrid:
            tasks += 1
            if task.get('completed'):
                completed += 1
                tasks_items.append(task.get('title'))
    print ('Employee {} is done with tasks({}/{}):'
           .format(emp_name, completed, tasks))

    for t in tasks_items:
        print('\t', t)
