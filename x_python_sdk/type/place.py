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
from x_python_sdk.type.geo import Geo
from x_python_sdk.type.place_type import PlaceType

class RequiredPlace(TypedDict):
    # The full name of this place.
    full_name: str

    # The identifier for this place.
    id: str

class OptionalPlace(TypedDict, total=False):
    contained_within: typing.List[str]

    # The full name of the county in which this place exists.
    country: str

    country_code: CountryCode

    geo: Geo

    # The human readable name of this place.
    name: str

    place_type: PlaceType

class Place(RequiredPlace, OptionalPlace):
    pass
