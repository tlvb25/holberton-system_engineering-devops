#!/usr/bin/env bash
import json
import requests


def number_of_subscribers(subreddit):
    """0. How many subs? """
    base_url = 'https://www.reddit.com/r/{}/.json'.format(subreddit)

    head = {'User-Agent': 'Reddit API test'}

    response = requests.get(base_url, headers=head, allow_redirects=False)

    json_dict = response.json()

    if json_dict.get('error', 200) == 404:
        return 0
    return json_dict.get('data').get('children')[0]\
                         .get('data').get('subreddit_subscribers')
