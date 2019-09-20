#!/usr/bin/python3
"""3. Count it! """
import requests


def recurse(subreddit, word_list, after="", dic={}):
    """recursive"""
    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    h = {'User-Agent': 'Reddit API test'}
    params = {'limit': 200, 'after': after}
    req_url = requests.get(base_url, headers=h,
                           allow_redirects=False, params=params)

    if req_url.status_code != 200:
        return None

    json_dict = req_url.json()

    if after is None:
        return dic

    results = json_dict.get('data', {}).get('children')

    for i in results:
        title = i.get('data', {}).get('title').lower().split()
        for java in word_list:
            for t in title:
                if java == t:
                    if java not in dic:
                        dic[java] = 1
                    else:
                        dic[j] += 1

    param = json_dict.get('data', {}).get('after')
    return recurse(subreddit, word_list, param, dic)


def count_words(subreddit, word_list):
    """counting keywords"""
    for i, e in enumerate(word_list):
        word_list[i] = e.lower()

    dictionary = recurse(subreddit, word_list)

    if dictionary:
        for key, value in sorted(dictionary.items(),
                                 key=lambda x: (-x[1], x[0])):
            print("{}: {}".format(key, value))
    elif dictionary is None:
        print()
