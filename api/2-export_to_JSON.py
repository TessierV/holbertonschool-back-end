#!/usr/bin/python3
"""
Write a Python script that,
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys


if __name__ == '__main__':
    """API"""
    """ EXTRACT USER DATA """
    emp_id = sys.argv[1]
    emp_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    extract_employee = requests.get(emp_url).json()

    """ FORMAT """
    EMPLOYEE_USERNAME = extract_employee.get('username')

    """ EXTRACT TASK """
    task_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(emp_id)
    extract_task = requests.get(task_url).json()

    with open("{}.json".format(emp_id), "w") as user_id:
        json.dump({emp_id: [{
                'task': i.get('title'),
                'completed': i.get('completed'),
                'username': EMPLOYEE_USERNAME
            } for i in extract_task]}, user_id)
