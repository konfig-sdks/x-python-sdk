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

from x_python_sdk.pydantic.list_id import ListId
from x_python_sdk.pydantic.user_id import UserId

class ModelList(BaseModel):
    id: ListId = Field(alias='id')

    # The name of this List.
    name: str = Field(alias='name')

    description: typing.Optional[str] = Field(None, alias='description')

    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    follower_count: typing.Optional[int] = Field(None, alias='follower_count')

    member_count: typing.Optional[int] = Field(None, alias='member_count')

    owner_id: typing.Optional[UserId] = Field(None, alias='owner_id')

    private: typing.Optional[bool] = Field(None, alias='private')
    class Config:
        arbitrary_types_allowed = True
