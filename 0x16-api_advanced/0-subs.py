#!/usr/bin/python3

import requests
def number_of_subscribers(subreddit):
    """code to get the number of subscribers in a subreddit"""
    
    base_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'vale/1.0.0'}
    
    requested = requests.get(base_url, headers=headers, allow_redirects=False)

    if requested.status_code != 200:
        return 0

    r_json = requested.json()
    
    data = r_json.get("data")

    subscribers = data.get("subscribers")
    return subscribers

