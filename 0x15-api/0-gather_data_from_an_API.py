#!/usr/bin/python3
"""
a Python script that uses a REST API,
for a given employee ID,
to return information about his/her TODO list progress.
"""
import argparse
import json
import requests


def get_employee_data(employee_id):
    url_us = 'https://jsonplaceholder.typicode.com/users/'
    url_u = url_us + str(employee_id)
    u_info = requests.get(url_u).json()
    u_name = u_info.get("name")
    u_t_url = url_us + str(employee_id) + '/todos/'
    u_todos = requests.get(u_t_url).json()
    return u_name, u_todos


def parse_arguments():
    parser = argparse.ArgumentParser(description='Get employee TODO list progress')
    parser.add_argument('employee_id', type=int, help='Employee ID')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    employee_id = args.employee_id

    employee_name, todos = get_employee_data(employee_id)

    n_c_todos = 0
    c_tasks = []

    for todo in todos:
        if todo.get("completed") is True:
            n_c_todos += 1
            c_tasks.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name,
        n_c_todos,
        len(todos)
    ))
    for task in c_tasks:
        print("\t{}".format(task))
