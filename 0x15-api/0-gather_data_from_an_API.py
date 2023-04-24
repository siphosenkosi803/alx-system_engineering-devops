#!/usr/bin/python3
"""
a Python script that uses a REST API, 
for a given employee ID,
to return information about his/her TODO list progress.
"""
import requests
import sys
from sys import argv

if __name__ == "__main__":

    _n_c_todos_ = 0
    _n_todos_ = 0
    _c_tasks_= []
    _url_us_ = 'https://jsonplaceholder.typicode.com/users/'
    _url_u_ = _url_us_ + sys.argv[1]
    _u_info_ = requests.get(_url_u_).json()

    _u_name_ = _u_info_.get("name")

    _u_t_url_ = _url_us_ + sys.argv[1] + '/todos/'
    _u_todos_ = requests.get(_u_t_url_).json()

    for _u_t_ in _u_todos_:
        _n_todos_ += 1
        if (_u_t_.get("completed") is True):
            _n_c_todos_ += 1
            _c_tasks_.append(_u_t_.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        _u_name_,
        _n_c_todos_,
        _n_todos_
        ))
    for task in _c_tasks_:
        print("\t {}".format(task))
