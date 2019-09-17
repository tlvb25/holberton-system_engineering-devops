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
        tasks = []
        for task in tasks_obj:
            if task.get('userId') == usrid:
                d = {"username": emp_name, "task": task.get('title'),
                     "completed": task.get('completed')}
                tasks.append(d)
        json_f[usrid] = tasks

    with open("todo_all_employees.json", mode='w') as file:
        json.dump(jsonDict, file)
