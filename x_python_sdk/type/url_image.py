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

from x_python_sdk.type.media_height import MediaHeight
from x_python_sdk.type.media_width import MediaWidth

class RequiredUrlImage(TypedDict):
    pass

class OptionalUrlImage(TypedDict, total=False):
    height: MediaHeight

    # A validly formatted URL.
    url: str

    width: MediaWidth

class UrlImage(RequiredUrlImage, OptionalUrlImage):
    pass
