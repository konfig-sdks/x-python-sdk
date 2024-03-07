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
from x_python_sdk.type.get2_users_id_followers_response_meta import Get2UsersIdFollowersResponseMeta
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.user import User

class RequiredGet2UsersIdFollowersResponse(TypedDict):
    pass

class OptionalGet2UsersIdFollowersResponse(TypedDict, total=False):
    data: typing.List[User]

    errors: typing.List[Problem]

    includes: Expansions

    meta: Get2UsersIdFollowersResponseMeta

class Get2UsersIdFollowersResponse(RequiredGet2UsersIdFollowersResponse, OptionalGet2UsersIdFollowersResponse):
    pass
