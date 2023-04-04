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
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    extract_employee = requests.get(employee_url).json()
    EMPLOYEE_NAME = extract_employee.get('name')

    """ EXTRACT TASK """
    task_url = "https://jsonplaceholder.typicode.com/todos/"
    extract_task = requests.get(task_url).json()

    """ Format """
    TASK_TITLE = []
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = len(extract_task)

    for i in extract_task:
        if i.get('completed') is True:
            TASK_TITLE.append(i['title'])
            NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for i in TASK_TITLE:
        print("\t {}".format(i))
