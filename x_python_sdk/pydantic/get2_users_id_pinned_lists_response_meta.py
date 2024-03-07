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


class Get2UsersIdPinnedListsResponseMeta(BaseModel):
    # The number of results returned in this response.
    result_count: typing.Optional[int] = Field(None, alias='result_count')
    class Config:
        arbitrary_types_allowed = True
