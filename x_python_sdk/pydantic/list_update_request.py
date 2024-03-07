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


class ListUpdateRequest(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    name: typing.Optional[str] = Field(None, alias='name')

    private: typing.Optional[bool] = Field(None, alias='private')
    class Config:
        arbitrary_types_allowed = True
