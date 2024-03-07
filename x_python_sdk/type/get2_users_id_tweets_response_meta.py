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

from x_python_sdk.type.next_token import NextToken
from x_python_sdk.type.previous_token import PreviousToken

class RequiredGet2UsersIdTweetsResponseMeta(TypedDict):
    pass

class OptionalGet2UsersIdTweetsResponseMeta(TypedDict, total=False):
    # The newest id in this response.
    newest_id: str

    next_token: NextToken

    # The oldest id in this response.
    oldest_id: str

    previous_token: PreviousToken

    # The number of results returned in this response.
    result_count: int

class Get2UsersIdTweetsResponseMeta(RequiredGet2UsersIdTweetsResponseMeta, OptionalGet2UsersIdTweetsResponseMeta):
    pass
