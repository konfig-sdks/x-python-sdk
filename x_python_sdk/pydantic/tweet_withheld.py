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

class TweetWithheld(BaseModel):
    # Indicates if the content is being withheld for on the basis of copyright infringement.
    copyright: bool = Field(alias='copyright')

    # Provides a list of countries where this content is not available.
    country_codes: typing.List[CountryCode] = Field(alias='country_codes')

    # Indicates whether the content being withheld is the `tweet` or a `user`.
    scope: typing.Optional[Literal["tweet", "user"]] = Field(None, alias='scope')
    class Config:
        arbitrary_types_allowed = True
