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

from x_python_sdk.type.media import Media
from x_python_sdk.type.place import Place
from x_python_sdk.type.poll import Poll
from x_python_sdk.type.topic import Topic
from x_python_sdk.type.tweet import Tweet
from x_python_sdk.type.user import User

class RequiredExpansions(TypedDict):
    pass

class OptionalExpansions(TypedDict, total=False):
    media: typing.List[Media]

    places: typing.List[Place]

    polls: typing.List[Poll]

    topics: typing.List[Topic]

    tweets: typing.List[Tweet]

    users: typing.List[User]

class Expansions(RequiredExpansions, OptionalExpansions):
    pass
