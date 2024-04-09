#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
 If an invalid subreddit is given, the function returns 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of active subscribers,
    return 0 if does not subreddit doesn't exist
    """
    # URL for subbreddit's about page
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # headers
    headers = {
        'Accept': 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers,
                            allow_redirects=False, timeout=10)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the subscriber count
        subscribers = data["data"]["subscribers"]

        return subscribers

    # If the subreddit is invalid or there's an error, return 0
    return 0
