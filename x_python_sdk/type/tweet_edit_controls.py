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


class RequiredTweetEditControls(TypedDict):
    # Time when Tweet is no longer editable.
    editable_until: datetime

    # Number of times this Tweet can be edited.
    edits_remaining: int

    # Indicates if this Tweet is eligible to be edited.
    is_edit_eligible: bool

class OptionalTweetEditControls(TypedDict, total=False):
    pass

class TweetEditControls(RequiredTweetEditControls, OptionalTweetEditControls):
    pass
