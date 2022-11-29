#!/usr/bin/python3
'''
Defines function that prints the top ten posts of a subreddit
'''
import requests


def top_ten(subreddit):
    '''Prints the top ten posts of a subreddit

    Return:
        None -  if the subreddit is invalid
    '''
    if subreddit is None or not isinstance(subreddit, str):
        return(None)
    endpoint = 'https://www.reddit.com'
    headers = {'user-agent': 'Mozilla/5.0 \
(Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    params = {'limit': 10}
    with requests.get('{}/r/{}/top.json'.format(endpoint, subreddit),
                      allow_redirects=False,
                      headers=headers,
                      params=params) as info:
        if info.status_code == 200:
            json_info = info.json()
            for post in json_info.get('data').get('children'):
                print(post.get('data').get('title'))
        else:
            print(None)
