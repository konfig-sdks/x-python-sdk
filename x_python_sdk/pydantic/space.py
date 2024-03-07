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

from x_python_sdk.pydantic.space_id import SpaceId
from x_python_sdk.pydantic.space_topics import SpaceTopics
from x_python_sdk.pydantic.user_id import UserId

class Space(BaseModel):
    id: SpaceId = Field(alias='id')

    # The current state of the Space.
    state: Literal["live", "scheduled", "ended"] = Field(alias='state')

    # The title of the Space.
    title: typing.Optional[str] = Field(None, alias='title')

    # Creation time of the Space.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    creator_id: typing.Optional[UserId] = Field(None, alias='creator_id')

    # End time of the Space.
    ended_at: typing.Optional[datetime] = Field(None, alias='ended_at')

    # The user ids for the hosts of the Space.
    host_ids: typing.Optional[typing.List[UserId]] = Field(None, alias='host_ids')

    # An array of user ids for people who were invited to a Space.
    invited_user_ids: typing.Optional[typing.List[UserId]] = Field(None, alias='invited_user_ids')

    # Denotes if the Space is a ticketed Space.
    is_ticketed: typing.Optional[bool] = Field(None, alias='is_ticketed')

    # The language of the Space.
    lang: typing.Optional[str] = Field(None, alias='lang')

    # The number of participants in a Space.
    participant_count: typing.Optional[int] = Field(None, alias='participant_count')

    # A date time stamp for when a Space is scheduled to begin.
    scheduled_start: typing.Optional[datetime] = Field(None, alias='scheduled_start')

    # An array of user ids for people who were speakers in a Space.
    speaker_ids: typing.Optional[typing.List[UserId]] = Field(None, alias='speaker_ids')

    # When the Space was started as a date string.
    started_at: typing.Optional[datetime] = Field(None, alias='started_at')

    # The number of people who have either purchased a ticket or set a reminder for this Space.
    subscriber_count: typing.Optional[int] = Field(None, alias='subscriber_count')

    topics: typing.Optional[SpaceTopics] = Field(None, alias='topics')

    # When the Space was last updated.
    updated_at: typing.Optional[datetime] = Field(None, alias='updated_at')
    class Config:
        arbitrary_types_allowed = True
