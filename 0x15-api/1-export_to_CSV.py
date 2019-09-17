#!/usr/bin/python3
"""Export to CSV"""
import csv
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

    with open('{}.csv'.format(argv[1]), mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for x, y in enumerate(tasks_items):
            writer.writerow([usrid, emp_name, completed[x], y])
