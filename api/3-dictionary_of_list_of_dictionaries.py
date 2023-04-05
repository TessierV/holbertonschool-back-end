#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data
in the JSON format.
"""
import json
import requests


if __name__ == '__main__':
    filename = "todo_all_employees.json"
    """ EXTRACT USER """
    emp_url = "https://jsonplaceholder.typicode.com/users/"
    extract_employee = requests.get(emp_url).json()

    """ EXTRACT TASK """
    task_url = "https://jsonplaceholder.typicode.com/todos"
    extract_task = requests.get(task_url).json()

    with open(filename, "w") as file:
        """ DICTIONNAIRE """
        dict_task = {i.get("id"): [{
            'task': j.get('title'),
            'completed': j.get('completed'),
            'username': i.get('username')}
            for j in extract_task
            if i.get("id") == j.get('userId')]
            for i in extract_employee}
        json.dump(dict_task, file)
    file.close()
