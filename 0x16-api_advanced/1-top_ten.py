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
        return 0
    try:
        r_json = requested.json()

        data = r_json.get("data")

        children = data.get("children")
        # print(children)
        for child in children[:10]:
            hot = child.get("data")
            print(hot.get("title"))
    except ValueError:
        print(None)
        return (None)
