#!/usr/bin/python3
"""
Returns the number of subs from Reddit API
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """Returns the number of subs"""
    url_base = 'https://www.reddit.com'
    query_url = 'r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "git/siphosenkosi803"}
    api_resp = requests.get(
        url='{}/{}'.format(url_base, query_url),
        headers=headers,
        allow_redirects=False
    )
    if api_resp.status_code == 200:
        json_api_data = api_resp.json().get("data")
        if json_api_data:
            return json_api_data.get("subscribers")
    return 0


if __name__ == '__main__':
    subreddit = sys.argv[1]
    print("{:d}".format(number_of_subscribers(subreddit)))
