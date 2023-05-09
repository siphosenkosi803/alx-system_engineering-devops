#!/usr/bin/python3
"""
Returns the titles of the first 10 hot posts
"""

import requests

def top_ten(subreddit):
    """Returns the top 10 hot posts"""
    url_base = 'https://www.reddit.com'
    query_url = 'r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "git/siphosenkosi803"}
    params = {"limit": 10}
    api_resp = requests.get(
        url='{}/{}'.format(url_base, query_url),
        headers=headers,
        params=params,
        allow_redirects=False)
    if api_resp.status_code == 200:
        json_api_data = api_resp.json().get("data")
        if json_api_data:
            bits = json_api_data.get("children")
            for bit in bits:
                print(bit.get("data").get("title"))
        else:
            print("None")
    else:
        print("None")


