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

from x_python_sdk.type.bookmark_mutation_response_data import BookmarkMutationResponseData
from x_python_sdk.type.problem import Problem

class RequiredBookmarkMutationResponse(TypedDict):
    pass

class OptionalBookmarkMutationResponse(TypedDict, total=False):
    data: BookmarkMutationResponseData

    errors: typing.List[Problem]

class BookmarkMutationResponse(RequiredBookmarkMutationResponse, OptionalBookmarkMutationResponse):
    pass
