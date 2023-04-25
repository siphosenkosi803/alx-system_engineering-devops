#!/usr/bin/python3
"""
script to export _d_ in tJSON format
."""
import json
import requests
import sys


if __name__ == "__main__":
    try:
        _u_i_ = sys.argv[1]
        _u_i_ = "https://jsonplaceholder.typicode.com/users/{}/".format(
            _u_i_)
        _r_ = requests.get(_u_i_).json()
        _u_n_ = _r_.get("_u_n_")
        _u_t_url_ = (
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                _u_i_)
        )
        _u_todos_ = requests.get(_u_t_url_).json()
        _f_n_ = "{}.json".format(_u_i_)
        _a_d_ = {}
        _d_l_ = []
        for todo in _u_todos_:
            print(todo)
            _d_ = {}
            _d_['task'] = todo.get('title')
            _d_['completed'] = todo.get('completed')
            _d_['_u_n_'] = _u_n_
            _d_l_.append(_d_)
        _a_d_[_u_i_] = _d_l_
        with open(_f_n_, 'w', encoding='utf-8') as f:
            json.dump(_a_d_, f)
    except ValueError:
        exit()
