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

from x_python_sdk.pydantic.poll_id import PollId
from x_python_sdk.pydantic.poll_option import PollOption

class Poll(BaseModel):
    id: PollId = Field(alias='id')

    options: typing.List[PollOption] = Field(alias='options')

    duration_minutes: typing.Optional[int] = Field(None, alias='duration_minutes')

    end_datetime: typing.Optional[datetime] = Field(None, alias='end_datetime')

    voting_status: typing.Optional[Literal["open", "closed"]] = Field(None, alias='voting_status')
    class Config:
        arbitrary_types_allowed = True
