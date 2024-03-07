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

from x_python_sdk.type.list_update_response_data import ListUpdateResponseData
from x_python_sdk.type.problem import Problem

class RequiredListUpdateResponse(TypedDict):
    pass

class OptionalListUpdateResponse(TypedDict, total=False):
    data: ListUpdateResponseData

    errors: typing.List[Problem]

class ListUpdateResponse(RequiredListUpdateResponse, OptionalListUpdateResponse):
    pass
