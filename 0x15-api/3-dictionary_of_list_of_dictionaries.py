#!/usr/bin/python3
"""
script to export data in json
"""
import json
import requests


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users",
                         verify=False).json()
    _u_d_ = {}
    _u_n_d = {}
    for user in users:
        _u_i_ = user.get("id")
        _u_d_[_u_i_] = []
        _u_n_d[_u_i_] = user.get("username")
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/tasks",
        verify=False).json()
    for guide in tasks:
        _t_dictionary_ = {}
        _u_i_ = guide.get("userId")
        _t_dictionary_["task"] = guide.get('title')
        _t_dictionary_["completed"] = guide.get('completed')
        _t_dictionary_["username"] = _u_n_d.get(_u_i_)
        _u_d_.get(_u_i_).append(_t_dictionary_)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(_u_d_, jsonfile)
