#!/usr/bin/python3
"""
Write a Python script that,
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == '__main__':
    """API"""
    """ EXTRACT USER DATA """
    employee_id = sys.argv[1]
    employee_url = "https://jsonplaceholder.typicode.com/users/{employee_id}"
    extract_employee = requests.get(employee_url).json()
    EMPLOYEE_NAME = extract_employee.get('name')

    """ EXTRACT TASK """
    task_url = "https://jsonplaceholder.typicode.com/todos/{employee_id}"
    extract_task = requests.get(task_url).json()

    """ Format """
    TASK_TITLE = []
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    for i in extract_task:
        if task.get('completed') is True:
            TASK_TITLE.append(i['title'])
            NUMBER_OF_DONE_TASKS += 1
        TOTAL_NUMBER_OF_TASKS += 1

    print("Employee {} is done with tasks({}/{}): \n\t {}"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS, TASK_TITLE))