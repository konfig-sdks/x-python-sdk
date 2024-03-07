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


class TweetHideResponseData(BaseModel):
    hidden: typing.Optional[bool] = Field(None, alias='hidden')
    class Config:
        arbitrary_types_allowed = True
