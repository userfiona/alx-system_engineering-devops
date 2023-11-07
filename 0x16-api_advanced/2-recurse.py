#!/usr/bin/python3
"""
This script uses the Reddit API to retrieve the top ten post titles from a specified subreddit recursively.
"""

import requests

after = None

def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieves the top ten post titles from the specified subreddit.

    :param subreddit: The name of the subreddit to fetch posts from.
    :param hot_list: A list to store the top post titles.
    :return: A list of the top post titles or None if there was an issue with the request.
    """
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return None
