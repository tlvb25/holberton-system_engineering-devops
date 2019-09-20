#!/usr/bin/python3
"""1. Top Ten"""
import requests


def top_ten(subreddit):
    """queries the Reddit API"""
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    header = {'User-Agent': 'Reddit API test'}

    params = {'limit': 10}

    response = requests.get(url, headers=header, allow_redirects=False, params=params)

    json_dict = response.json()

    if json_dict.get('error', 200) == 404:
        print(None)
        return

    results = json_dict.get('data').get('children')

    for dic in results[:10]:
        print(dic.get('data').get('title'))
