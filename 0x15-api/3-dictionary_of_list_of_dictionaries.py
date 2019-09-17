#!/usr/bin/python3
""" Dictionary of list of dictionaries """
import json
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get('https://jsonplaceholder.typicode.com/users')

    name_obj = response.json()

    response = requests.get('https://jsonplaceholder.typicode.com/todos')

    tasks_obj = response.json()

    jsonDict = {}

    for n in name_obj:
        usrid = n.get('id')
        emp_name = n.get('username')
        tasks_items = []
        for task_items in tasks_obj:
            if task_items.get('userId') == usrid:
                d = {"username": emp_name, "task": task_items.get('title'),
                     "completed": task_items.get('completed')}
                tasks_items.append(d)
        json_f[usrid] = tasks_items

    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump(jsonDict, json_file)
