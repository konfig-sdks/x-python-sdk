# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.62
    Created by: https://developer.twitter.com/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from x_python_sdk.type.media_id import MediaId
from x_python_sdk.type.user_id import UserId

class RequiredTweetCreateRequestMedia(TypedDict):
    # A list of Media Ids to be attached to a created Tweet.
    media_ids: typing.List[MediaId]

class OptionalTweetCreateRequestMedia(TypedDict, total=False):
    # A list of User Ids to be tagged in the media for created Tweet.
    tagged_user_ids: typing.List[UserId]

class TweetCreateRequestMedia(RequiredTweetCreateRequestMedia, OptionalTweetCreateRequestMedia):
    pass
