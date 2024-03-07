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

from x_python_sdk.type.list_create_response_data import ListCreateResponseData
from x_python_sdk.type.problem import Problem

class RequiredListCreateResponse(TypedDict):
    pass

class OptionalListCreateResponse(TypedDict, total=False):
    data: ListCreateResponseData

    errors: typing.List[Problem]

class ListCreateResponse(RequiredListCreateResponse, OptionalListCreateResponse):
    pass
