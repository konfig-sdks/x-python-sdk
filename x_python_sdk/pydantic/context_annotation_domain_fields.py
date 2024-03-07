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


class ContextAnnotationDomainFields(BaseModel):
    # The unique id for a context annotation domain.
    id: str = Field(alias='id')

    # Description of the context annotation domain.
    description: typing.Optional[str] = Field(None, alias='description')

    # Name of the context annotation domain.
    name: typing.Optional[str] = Field(None, alias='name')
    class Config:
        arbitrary_types_allowed = True
