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

from x_python_sdk.type.full_text_entities import FullTextEntities
from x_python_sdk.type.user_entities_url import UserEntitiesUrl

class RequiredUserEntities(TypedDict):
    pass

class OptionalUserEntities(TypedDict, total=False):
    description: FullTextEntities

    url: UserEntitiesUrl

class UserEntities(RequiredUserEntities, OptionalUserEntities):
    pass
