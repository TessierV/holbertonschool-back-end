#!/usr/bin/python3
"""
Write a Python script that,
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
import sys

if __name__ == '__main__':
    # Extract employee data from the API
    emp_id = sys.argv[1]
    emp_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    with requests.get(emp_url) as response:
        extract_employee = response.json()
    EMPLOYEE_NAME = extract_employee.get('name')

    # Extract tasks from the API and write to CSV file
    task_url = f"https://jsonplaceholder.typicode.com/todos/?userId={emp_id}"
    with requests.get(task_url) as response:
        extract_task = response.json()
    with open(f"{emp_id}.csv", mode='w') as fil:
        field = ['emp_id', 'employee_name', 'completed', 'title']
        writer = csv.DictWriter(fil, fieldnames=field, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        for task in extract_task:
            if task.get('userId') == int(emp_id):
                writer.writerow({
                    'emp_id': emp_id,
                    'employee_name': EMPLOYEE_NAME,
                    'completed': task.get('completed'),
                    'title': task.get('title')
                })
