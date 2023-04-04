#!/usr/bin/python3
"""
Write a Python script that,
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys
import csv


if __name__ == '__main__':
    """ Format """

    TASK_TITLE = []
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    """API"""
    """ EXTRACT USER DATA """
    emp_id = sys.argv[1]
    emp_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    extract_employee = requests.get(emp_url).json()
    EMPLOYEE_NAME = extract_employee.get('name')

    """ EXTRACT TASK """
    task_url = "https://jsonplaceholder.typicode.com/todos/"
    extract_task = requests.get(task_url).json()

    with open('{}.csv'.format(emp_id), mode='w') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for i in extract_task:
            if i.get('userId') == int(emp_id):
                writer.writerow({'USER_ID': emp_id, 'USERNAME': EMPLOYEE_NAME,
                                 'TASK_COMPLETED_STATUS': i.get('completed'), 'TASK_TITLE': i.get('title')})
    print("Employee {}'s task data has been exported to {}.csv".format(EMPLOYEE_NAME, emp_id))
