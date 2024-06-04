#!/usr/bin/python3
"""code to get the top 10 hottest post on a subreddit"""

import requests


def top_ten(subreddit):
    """code to get the number of subscribers in a subreddit"""

    base_url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    headers = {'User-Agent': 'vale/1.0.0'}

    requested = requests.get(base_url, headers=headers, allow_redirects=False)

    if requested.status_code != 200:
        print(None)
        return None

    try:
        js = requested.json()

    except ValueError:
        print(None)
        return None

    try:

        data = js.get("data")
        children = data.get("children")
        for child in children[:10]:
            post = child.get("data")
            print(post.get("title"))

    except:
        print(None)
