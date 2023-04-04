#!/usr/bin/python3
"""
Write a Python script that, using this extract_employeeT API,
for a given employee ID, returns information about
his/her TODO list progextract_employees
export data in the CSV format.
"""
import csv
import requests
import sys


if __name__ == '__main__':
    """ EXTRACT USER DATA """
    emp_id = sys.argv[1]
    emp_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    extract_employee = requests.get(emp_url).json()
    EMPLOYEE_NAME = extract_employee.get("username")

    """ EXTRACT TASK """
    extract_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
        + '/todos')
    with open("{}.csv".format(sys.argv[1]), "w") as file_c:
        writer = csv.writer(file_c, quoting=csv.QUOTE_ALL)
        for task in extract_employee.json():
            writer.writerow([emp_id, EMPLOYEE_NAME,
                            task.get("completed"), task.get("title")])
