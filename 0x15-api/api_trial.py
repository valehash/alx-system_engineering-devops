#!/usr/bin/python3
import requests
import sys

def make_request(resource, param=None):
        """Retrieve user from API
        """
        url = 'https://jsonplaceholder.typicode.com/'
        url += resource
        if param:
            url += ('?' + param[0] + '=' + param[1])

        # make request
        print(url)
        r = requests.get(url)

        # extract json response
        r = r.json()
        return r

user = make_request('users', ('id', sys.argv[1])) 
print(user)
