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


class RequiredListCreateRequest(TypedDict):
    name: str

class OptionalListCreateRequest(TypedDict, total=False):
    description: str

    private: bool

class ListCreateRequest(RequiredListCreateRequest, OptionalListCreateRequest):
    pass
