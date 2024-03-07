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


class RequiredListUnpinResponseData(TypedDict):
    pass

class OptionalListUnpinResponseData(TypedDict, total=False):
    pinned: bool

class ListUnpinResponseData(RequiredListUnpinResponseData, OptionalListUnpinResponseData):
    pass
