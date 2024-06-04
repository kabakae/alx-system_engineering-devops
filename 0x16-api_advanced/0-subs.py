#!/usr/bin/python3
"""
This module provides a function to query the the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscrib subreddit.
    If an invalid subreddit is given, the function returns 0.

    Args:
        subreddit (str): The subreddit name.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": ("python:subreddit.subscriber.count:v1.0 "
                       "(by /u/yourusername)")
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print(f"Response Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Data: {data}")  # Debugging line
            return data["data"]["subscribers"]
        elif response.status_code == 403:
            print(f"Error: {response.status_code} - Forbidden. Ensure "
                  "User-Agent is correct.")  # Debugging line
            return 0
        else:
            print(f"Error: {response.status_code} - {response.reason}")
            return 0
    except requests.RequestException as e:
        print(f"Request Exception: {e}")  # Debugging line
        return 0
