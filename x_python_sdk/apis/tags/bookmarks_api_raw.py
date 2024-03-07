# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.62
    Created by: https://developer.twitter.com/
"""

from x_python_sdk.paths._2_users_id_bookmarks.post import AddTweetRaw
from x_python_sdk.paths._2_users_id_bookmarks.get import GetUserBookmarksRaw
from x_python_sdk.paths._2_users_id_bookmarks_tweet_id.delete import RemoveTweetRaw


class BookmarksApiRaw(
    AddTweetRaw,
    GetUserBookmarksRaw,
    RemoveTweetRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
