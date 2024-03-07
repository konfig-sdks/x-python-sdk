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
from x_python_sdk.type.get2_users_id_muting_response_meta import Get2UsersIdMutingResponseMeta
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.user import User

class RequiredGet2UsersIdMutingResponse(TypedDict):
    pass

class OptionalGet2UsersIdMutingResponse(TypedDict, total=False):
    data: typing.List[User]

    errors: typing.List[Problem]

    includes: Expansions

    meta: Get2UsersIdMutingResponseMeta

class Get2UsersIdMutingResponse(RequiredGet2UsersIdMutingResponse, OptionalGet2UsersIdMutingResponse):
    pass
