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
from x_python_sdk.type.users_likes_delete_response_data import UsersLikesDeleteResponseData

class RequiredUsersLikesDeleteResponse(TypedDict):
    pass

class OptionalUsersLikesDeleteResponse(TypedDict, total=False):
    data: UsersLikesDeleteResponseData

    errors: typing.List[Problem]

class UsersLikesDeleteResponse(RequiredUsersLikesDeleteResponse, OptionalUsersLikesDeleteResponse):
    pass
