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

from x_python_sdk.pydantic.next_token import NextToken
from x_python_sdk.pydantic.previous_token import PreviousToken

class Get2UsersIdTimelinesReverseChronologicalResponseMeta(BaseModel):
    # The newest id in this response.
    newest_id: typing.Optional[str] = Field(None, alias='newest_id')

    next_token: typing.Optional[NextToken] = Field(None, alias='next_token')

    # The oldest id in this response.
    oldest_id: typing.Optional[str] = Field(None, alias='oldest_id')

    previous_token: typing.Optional[PreviousToken] = Field(None, alias='previous_token')

    # The number of results returned in this response.
    result_count: typing.Optional[int] = Field(None, alias='result_count')
    class Config:
        arbitrary_types_allowed = True
