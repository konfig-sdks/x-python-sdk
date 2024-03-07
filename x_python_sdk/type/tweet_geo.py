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

from x_python_sdk.type.point import Point

class RequiredTweetGeo(TypedDict):
    pass

class OptionalTweetGeo(TypedDict, total=False):
    coordinates: Point

    # The identifier for this place.
    place_id: str

class TweetGeo(RequiredTweetGeo, OptionalTweetGeo):
    pass
