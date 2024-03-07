# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.62
    Created by: https://developer.twitter.com/
"""

from x_python_sdk.paths._2_users_id_bookmarks.post import AddTweet
from x_python_sdk.paths._2_users_id_bookmarks.get import GetUserBookmarks
from x_python_sdk.paths._2_users_id_bookmarks_tweet_id.delete import RemoveTweet
from x_python_sdk.apis.tags.bookmarks_api_raw import BookmarksApiRaw


class BookmarksApi(
    AddTweet,
    GetUserBookmarks,
    RemoveTweet,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: BookmarksApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = BookmarksApiRaw(api_client)
