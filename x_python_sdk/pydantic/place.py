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
from pydantic import BaseModel, Field, RootModel

from x_python_sdk.pydantic.country_code import CountryCode
from x_python_sdk.pydantic.geo import Geo
from x_python_sdk.pydantic.place_type import PlaceType

class Place(BaseModel):
    # The full name of this place.
    full_name: str = Field(alias='full_name')

    # The identifier for this place.
    id: str = Field(alias='id')

    contained_within: typing.Optional[typing.List[str]] = Field(None, alias='contained_within')

    # The full name of the county in which this place exists.
    country: typing.Optional[str] = Field(None, alias='country')

    country_code: typing.Optional[CountryCode] = Field(None, alias='country_code')

    geo: typing.Optional[Geo] = Field(None, alias='geo')

    # The human readable name of this place.
    name: typing.Optional[str] = Field(None, alias='name')

    place_type: typing.Optional[PlaceType] = Field(None, alias='place_type')
    class Config:
        arbitrary_types_allowed = True
