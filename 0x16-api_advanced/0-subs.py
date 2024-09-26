#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit

    Parameters:
    subreddit (str): The subreddit to retrieve the number of subscribers for

    Returns:
    int: The number of subscribers for the given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    try:
        url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
        headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        json_data = response.json()
        subs = json_data.get("data", {}).get("subscribers", 0)
        return subs

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
