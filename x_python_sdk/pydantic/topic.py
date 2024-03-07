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


class Topic(BaseModel):
    # Unique identifier of this Topic.
    id: str = Field(alias='id')

    # The name of the given topic.
    name: str = Field(alias='name')

    # The description of the given topic.
    description: typing.Optional[str] = Field(None, alias='description')
    class Config:
        arbitrary_types_allowed = True
