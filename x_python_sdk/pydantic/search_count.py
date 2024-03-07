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


class SearchCount(BaseModel):
    # The end time of the bucket.
    end: datetime = Field(alias='end')

    # The start time of the bucket.
    start: datetime = Field(alias='start')

    # The count for the bucket.
    tweet_count: int = Field(alias='tweet_count')
    class Config:
        arbitrary_types_allowed = True
