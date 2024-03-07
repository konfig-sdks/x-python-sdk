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

class RequiredGet2TweetsIdQuoteTweetsResponseMeta(TypedDict):
    pass

class OptionalGet2TweetsIdQuoteTweetsResponseMeta(TypedDict, total=False):
    next_token: NextToken

    # The number of results returned in this response.
    result_count: int

class Get2TweetsIdQuoteTweetsResponseMeta(RequiredGet2TweetsIdQuoteTweetsResponseMeta, OptionalGet2TweetsIdQuoteTweetsResponseMeta):
    pass
