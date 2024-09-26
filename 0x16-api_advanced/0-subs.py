#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    try:
        r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                         headers={'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'})

        r.raise_for_status()  # Raise an exception for bad status codes

        json_data = r.json()
        subs = json_data.get("data", {}).get("subscribers", 0)
        return subs

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
