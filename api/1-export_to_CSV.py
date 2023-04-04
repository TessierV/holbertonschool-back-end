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

    with open("{}.csv".format(emp_id), mode='w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for i in extract_task:
            writer.writerow([emp_id, EMPLOYEE_NAME,
                            i.get("completed"), i.get("title")])
