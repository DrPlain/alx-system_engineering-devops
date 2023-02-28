#!/usr/bin/python3
"""Queries reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Queries reddit API and returns no of subs for a given a reddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    r = requests.get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers={'User-Agent': 'DrPlain'}).json()
    subs = r.get('data', {}).get('subscribers', 0)
    return subs
