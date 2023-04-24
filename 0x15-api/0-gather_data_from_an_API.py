#!/usr/bin/python3
"""Script that, usingAPI, for a given employee ID,
   returns information about his."""
import requests
import sys
from sys import argv

if __name__ == '__main__':
    app = 'https://jsonplaceholder.typicode.com'
    userR_ = requests.get(app + '/users/' + argv[1]).json()
    todos_ = requests.get(app + '/todos?userId=' + argv[1]).json()

    _tt = [_todo['title'] for _todo in todos_ if _todo['completed']]

    print('Employee {} is done with tasks({}/{}):'
          .format(userR_['name'], len(_tt), len(todos_)))

    [print('\t {}'.format(title)) for title in _tt]
