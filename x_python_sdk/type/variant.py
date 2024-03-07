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


class RequiredVariant(TypedDict):
    pass

class OptionalVariant(TypedDict, total=False):
    # The bit rate of the media.
    bit_rate: int

    # The content type of the media.
    content_type: str

    # The url to the media.
    url: str

class Variant(RequiredVariant, OptionalVariant):
    pass
