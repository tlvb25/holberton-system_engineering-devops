#!/usr/bin/python3
"""Recurse it!"""

import json
import requests


def recurse(subreddit, hot_list=[], after=""):
    """2. Recurse it! """
    base_url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    header = {'User-Agent': 'Reddit API test'}

    params = {'limit': 200, 'after': after}
    r = requests.get(base_url, headers=header,
                     allow_redirects=False, params=params)

    json_dict = r.json()

    if json_dict.get('error', 200) == 404:
        return None

    if after is None:
        return hot_list

    results = json_dict.get('data').get('children')

    for dic in results:
        hot_list.append(dic.get('data').get('title'))

    p = json_dict.get('data').get('after')
    return recurse(subreddit, hot_list, p)
