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


class EntityIndicesInclusiveExclusive(BaseModel):
    # Index (zero-based) at which position this entity ends.  The index is exclusive.
    end: int = Field(alias='end')

    # Index (zero-based) at which position this entity starts.  The index is inclusive.
    start: int = Field(alias='start')
    class Config:
        arbitrary_types_allowed = True
