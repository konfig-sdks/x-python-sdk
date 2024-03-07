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

from x_python_sdk.type.country_code import CountryCode

class RequiredUserWithheld(TypedDict):
    # Provides a list of countries where this content is not available.
    country_codes: typing.List[CountryCode]

class OptionalUserWithheld(TypedDict, total=False):
    # Indicates that the content being withheld is a `user`.
    scope: str

class UserWithheld(RequiredUserWithheld, OptionalUserWithheld):
    pass
