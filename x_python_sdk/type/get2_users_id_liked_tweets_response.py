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

from x_python_sdk.type.expansions import Expansions
from x_python_sdk.type.get2_users_id_liked_tweets_response_meta import Get2UsersIdLikedTweetsResponseMeta
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.tweet import Tweet

class RequiredGet2UsersIdLikedTweetsResponse(TypedDict):
    pass

class OptionalGet2UsersIdLikedTweetsResponse(TypedDict, total=False):
    data: typing.List[Tweet]

    errors: typing.List[Problem]

    includes: Expansions

    meta: Get2UsersIdLikedTweetsResponseMeta

class Get2UsersIdLikedTweetsResponse(RequiredGet2UsersIdLikedTweetsResponse, OptionalGet2UsersIdLikedTweetsResponse):
    pass
