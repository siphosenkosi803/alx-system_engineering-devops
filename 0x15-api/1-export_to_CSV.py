#!/usr/bin/python3
"""
export data in CSV format.
"""
import csv
import requests
import sys
from sys import argv


if __name__ == "__main__":
    _url_us_ = 'https://jsonplaceholder.typicode.com/users/'
    USER_ID = sys.argv[1]
    USERNAME = requests.get(_url_us_ + USER_ID).json().get("username")
    _u_t_url_ = _url_us_ + USER_ID + '/todos/'
    _u_todos_ = requests.get(_u_t_url_).json()
    file_name = "{}.csv".format(USER_ID)
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for _u_t_ in _u_todos_:
            writer.writerow([USER_ID, USERNAME,
                             str(_u_t_.get("completed")),
                             _u_t_.get("title")])
