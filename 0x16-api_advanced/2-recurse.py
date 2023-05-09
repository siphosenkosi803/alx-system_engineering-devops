#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns a list containing the titles of
all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API"""
    url_base = 'https://www.reddit.com'
    query_url = 'r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "git/siphosenkosi803"}
    params = {"limit": 100, "after": after}
    api_resp = requests.get(
        url='{}/{}'.format(url_base, query_url),
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if api_resp.status_code == 200:
        json_api_data = api_resp.json().get("data")
        if json_api_data:
            bits = json_api_data.get("children")
            hot_list += [bit.get("data").get("title") for bit in bits]
            after = json_api_data.get("after")
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    else:
        return None

if __name__ == '__main___':
    recurse(subreedit)

