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


class RequiredGet2SpacesSearchResponseMeta(TypedDict):
    pass

class OptionalGet2SpacesSearchResponseMeta(TypedDict, total=False):
    # The number of results returned in this response.
    result_count: int

class Get2SpacesSearchResponseMeta(RequiredGet2SpacesSearchResponseMeta, OptionalGet2SpacesSearchResponseMeta):
    pass
