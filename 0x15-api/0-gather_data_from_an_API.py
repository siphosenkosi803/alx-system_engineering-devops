#!/usr/bin/python3
  2 
  3 import requests
  4 import sys
  5 
  6 
  7 if __name__ == "__main__":
  8     # Check if an employee ID was provided as a command-line argument
  9     if len(sys.argv) < 2:
 10         print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
 11         sys.exit(1)
 12 
 13     # Set the base URL for the API
 14     api_url = "https://jsonplaceholder.typicode.com"
 15 
 16     # Get the employee ID from the command-line arguments
 17     employee_id = sys.argv[1]
 18 
 19     # Make an API request to get information about the employee
 20     response = requests.get("{}/users/{}".format(api_url, employee_id))
 21     employee = response.json()
 22 
 23     # Make an API request to get the employee's tasks
 24     response = requests.get("{}/todos".format(api_url) 
 25     params={"userId": employee_id})
 26     tasks = response.json()
 27     
 28     # Filter the tasks to get only the completed tasks
 29     completed_tasks = [task for task in tasks if task["completed"]]
 30     
 31     # Print out information about the employee and their completed tasks
 32     print("Employee {} is done with tasks({}/{}):".format(
 33         employee["name"], len(completed_tasks), len(tasks)))
 34     for task in completed_tasks:
 35         print("\t {}".format(task["title"]))
