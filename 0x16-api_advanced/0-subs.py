#!/usr/bin/python3
""" advanced api script for quering the the Reddit API and returns the number of subs"""
import requests
import sys


def number_of_subscribers(subreddit):
    """this function will return the number of subs"""
    _url_base_ = 'https://www.reddit.com'
    _my_query_url_ = 'r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "git/siphosenkosi803"}
    _api_resp_ = requests.get(
            url='{}/{}'.format(_url_base_, _my_query_url_),
            allow_redirects=False,
            headers=headers
            )
    if _api_resp_.status_code == 200:
        JSON_api_data = _api_resp_.json().get("data")
        if JSON_api_data:
            return JSON_api_data.get("subscribers")
    return 0

