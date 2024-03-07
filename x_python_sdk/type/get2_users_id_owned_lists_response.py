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
from x_python_sdk.type.get2_users_id_owned_lists_response_meta import Get2UsersIdOwnedListsResponseMeta
from x_python_sdk.type.model_list import ModelList
from x_python_sdk.type.problem import Problem

class RequiredGet2UsersIdOwnedListsResponse(TypedDict):
    pass

class OptionalGet2UsersIdOwnedListsResponse(TypedDict, total=False):
    data: typing.List[ModelList]

    errors: typing.List[Problem]

    includes: Expansions

    meta: Get2UsersIdOwnedListsResponseMeta

class Get2UsersIdOwnedListsResponse(RequiredGet2UsersIdOwnedListsResponse, OptionalGet2UsersIdOwnedListsResponse):
    pass
