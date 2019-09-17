#!/usr/bin/env bash
from sys import argv
import requests

if __name__ == "__main__":
    response = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(argv[1]))

    json_obj = response.json()

    emp_name = json_obj.get('name')

    tasks, completed = 0, 0

    tasks_items = []

    for task in json_obj:
        tasks += 1
        if task.get('completed'):
                completed += 1
                tasks_items.append(task.get('title'))
    print ('Employee {} is done with tasks({}/{}}):'
           .format(emp_name, completed, tasks))

    for t in tasks_items:
        print('\t', t)
