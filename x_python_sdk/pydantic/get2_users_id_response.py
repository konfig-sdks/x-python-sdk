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

from x_python_sdk.pydantic.expansions import Expansions
from x_python_sdk.pydantic.problem import Problem
from x_python_sdk.pydantic.user import User

class Get2UsersIdResponse(BaseModel):
    data: typing.Optional[User] = Field(None, alias='items')

    errors: typing.Optional[typing.List[Problem]] = Field(None, alias='errors')

    includes: typing.Optional[Expansions] = Field(None, alias='includes')
    class Config:
        arbitrary_types_allowed = True
