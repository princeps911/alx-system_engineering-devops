#!/usr/bin/python3
"""
Contains the top_ten function
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit

    Parameters:
    subreddit (str): The subreddit to retrieve the top 10 hot posts for
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    try:
        url = 'http://www.reddit.com/r/{}/hot/.json'.format(subreddit)
        headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'}
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        json_data = response.json()
        posts = json_data.get("data", {}).get("children", [])
        for post in posts[:10]:
            print(post.get("data", {}).get("title", ""))

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(None)
        else:
            print(f"Error: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
