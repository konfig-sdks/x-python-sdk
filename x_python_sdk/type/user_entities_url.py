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

from x_python_sdk.type.url_entity import UrlEntity

class RequiredUserEntitiesUrl(TypedDict):
    pass

class OptionalUserEntitiesUrl(TypedDict, total=False):
    urls: typing.List[UrlEntity]

class UserEntitiesUrl(RequiredUserEntitiesUrl, OptionalUserEntitiesUrl):
    pass
