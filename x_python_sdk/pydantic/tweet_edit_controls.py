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


class TweetEditControls(BaseModel):
    # Time when Tweet is no longer editable.
    editable_until: datetime = Field(alias='editable_until')

    # Number of times this Tweet can be edited.
    edits_remaining: int = Field(alias='edits_remaining')

    # Indicates if this Tweet is eligible to be edited.
    is_edit_eligible: bool = Field(alias='is_edit_eligible')
    class Config:
        arbitrary_types_allowed = True
