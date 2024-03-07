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

from x_python_sdk.type.media_key import MediaKey
from x_python_sdk.type.poll_id import PollId

class RequiredTweetAttachments(TypedDict):
    pass

class OptionalTweetAttachments(TypedDict, total=False):
    # A list of Media Keys for each one of the media attachments (if media are attached).
    media_keys: typing.List[MediaKey]

    # A list of poll IDs (if polls are attached).
    poll_ids: typing.List[PollId]

class TweetAttachments(RequiredTweetAttachments, OptionalTweetAttachments):
    pass
