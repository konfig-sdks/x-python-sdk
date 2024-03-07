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

from x_python_sdk.type.list_id import ListId
from x_python_sdk.type.user_id import UserId

class RequiredModelList(TypedDict):
    id: ListId

    # The name of this List.
    name: str

class OptionalModelList(TypedDict, total=False):
    description: str

    created_at: datetime

    follower_count: int

    member_count: int

    owner_id: UserId

    private: bool

class ModelList(RequiredModelList, OptionalModelList):
    pass
