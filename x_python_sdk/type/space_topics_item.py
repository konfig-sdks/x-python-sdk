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


class RequiredSpaceTopicsItem(TypedDict):
    # An ID suitable for use in the REST API.
    id: str

    # The name of the given topic.
    name: str

class OptionalSpaceTopicsItem(TypedDict, total=False):
    # The description of the given topic.
    description: str

class SpaceTopicsItem(RequiredSpaceTopicsItem, OptionalSpaceTopicsItem):
    pass
