#!/usr/bin/python3
'''
Defines function that queries the Reddit API and returns the
number of subscribers
'''
import requests
import sys


def number_of_subscribers(subreddit):
    '''Queries the Reddit API and returns the
    number of subscribers
    Return:
        0 - if invalid subreddit is given
    '''
    endpoint = 'https://www.reddit.com'
    sub_reddit = sys.argv[1]
    headers = {'user-agent': 'Mozilla/5.0 \
(Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    with requests.get('{}/r/{}/about.json'.format(
            endpoint,
            sub_reddit), headers=headers, allow_redirects=False) as info:
        if info.status_code == 200:
            json_info = info.json()
            return(json_info.get('data').get('subscribers'))
        else:
            return(0)
