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

from x_python_sdk.type.problem import Problem
from x_python_sdk.type.users_likes_create_response_data import UsersLikesCreateResponseData

class RequiredUsersLikesCreateResponse(TypedDict):
    pass

class OptionalUsersLikesCreateResponse(TypedDict, total=False):
    data: UsersLikesCreateResponseData

    errors: typing.List[Problem]

class UsersLikesCreateResponse(RequiredUsersLikesCreateResponse, OptionalUsersLikesCreateResponse):
    pass
