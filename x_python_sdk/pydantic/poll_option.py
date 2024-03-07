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

from x_python_sdk.pydantic.poll_option_label import PollOptionLabel

class PollOption(BaseModel):
    label: PollOptionLabel = Field(alias='label')

    # Position of this choice in the poll.
    position: int = Field(alias='position')

    # Number of users who voted for this choice.
    votes: int = Field(alias='votes')
    class Config:
        arbitrary_types_allowed = True
