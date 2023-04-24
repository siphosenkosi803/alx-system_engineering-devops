#!/usr/bin/python3
"""
Python script that uses a REST API to retrieve information about an employee's
TODO list progress based on their employee ID.
"""

import requests
import sys


if __name__ == "__main__":
    # Check if an employee ID was provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    # Set the base URL for the API
    _url = "https://jsonplaceholder.typicode.com"

    # Get the employee ID from the command-line arguments
    employee_id = sys.argv[1]

    # Make an API request to get information about the employee
    re_ = requests.get("{}/users/{}".format(_url, employee_id))
    employee = re_.json()

    # Make an API request to get the employee's tasks
    re_ = requests.get("{}/todos".format(_url), params={"userId": employee_id})
    tasks = response.json()

    # Filter the tasks to get only the completed tasks
    completed_tasks = [task for task in tasks if task["completed"]]

    # Print out information about the employee and their completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        employee["name"], len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print("\t {}".format(task["title"]))
