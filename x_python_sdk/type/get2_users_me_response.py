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
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.user import User

class RequiredGet2UsersMeResponse(TypedDict):
    pass

class OptionalGet2UsersMeResponse(TypedDict, total=False):
    items: User

    errors: typing.List[Problem]

    includes: Expansions

class Get2UsersMeResponse(RequiredGet2UsersMeResponse, OptionalGet2UsersMeResponse):
    pass
