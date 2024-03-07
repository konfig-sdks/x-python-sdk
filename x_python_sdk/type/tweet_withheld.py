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

from x_python_sdk.type.country_code import CountryCode

class RequiredTweetWithheld(TypedDict):
    # Indicates if the content is being withheld for on the basis of copyright infringement.
    copyright: bool

    # Provides a list of countries where this content is not available.
    country_codes: typing.List[CountryCode]

class OptionalTweetWithheld(TypedDict, total=False):
    # Indicates whether the content being withheld is the `tweet` or a `user`.
    scope: str

class TweetWithheld(RequiredTweetWithheld, OptionalTweetWithheld):
    pass
