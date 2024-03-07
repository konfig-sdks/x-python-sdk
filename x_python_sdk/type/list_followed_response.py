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

from x_python_sdk.type.list_followed_response_data import ListFollowedResponseData
from x_python_sdk.type.problem import Problem

class RequiredListFollowedResponse(TypedDict):
    pass

class OptionalListFollowedResponse(TypedDict, total=False):
    data: ListFollowedResponseData

    errors: typing.List[Problem]

class ListFollowedResponse(RequiredListFollowedResponse, OptionalListFollowedResponse):
    pass
