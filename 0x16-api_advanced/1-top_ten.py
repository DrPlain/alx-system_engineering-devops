#!/usr/bin/python3
"""Queries reddit API"""
import requests


def top_ten(subreddit):
    if subreddit is None or type(subreddit) is not str:
        print(None)
    res = requests.get('https://www.reddit.com/r/{}/hot/.json'.format(
        subreddit), headers={'User-Agent': 'Gideon'},
        allow_redirects=False, params={'limit': 10})

    if res.status_code > 200:
        print(None)
        return

    result = res.json().get('data')
    for child in result.get('children'):
        print(child.get('data').get('title'))
