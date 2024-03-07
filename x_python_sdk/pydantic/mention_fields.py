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

from x_python_sdk.pydantic.user_id import UserId
from x_python_sdk.pydantic.user_name import UserName

class MentionFields(BaseModel):
    username: UserName = Field(alias='username')

    id: typing.Optional[UserId] = Field(None, alias='id')
    class Config:
        arbitrary_types_allowed = True
