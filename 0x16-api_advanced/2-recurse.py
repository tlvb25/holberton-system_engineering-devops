#!/usr/bin/python3
"""Recurse it!"""

import json
import requests


def recurse(subreddit, hot_list=[], after=""):
    """recursive function that queries the Reddit API and returns a list
       containing the titles of all hot articles for a given subreddit. If no
       results are found for the given subreddit, the function should
       return None."""

    h = {"User-Agent": "Holberton-User"}

    params = {"after": after}

    base_url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    request = requests.get(base_url, params=params,
                           headers=h, allow_redirects=False)

    if request.status_code >= 300:
        return (None)

    req_url = req_url.json()

    if after is None:
        return (hot_list)

    listing = req_url.get('data').get('children')
    for dic in listing:
        hot_list.append(dic.get('data').get('title'))
    p = req_url.get('data').get('after')
    return recurse(subreddit, hot_list, p)
