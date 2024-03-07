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

from x_python_sdk.type.space_id import SpaceId
from x_python_sdk.type.space_topics import SpaceTopics
from x_python_sdk.type.user_id import UserId

class RequiredSpace(TypedDict):
    id: SpaceId

    # The current state of the Space.
    state: str

class OptionalSpace(TypedDict, total=False):
    # The title of the Space.
    title: str

    # Creation time of the Space.
    created_at: datetime

    creator_id: UserId

    # End time of the Space.
    ended_at: datetime

    # The user ids for the hosts of the Space.
    host_ids: typing.List[UserId]

    # An array of user ids for people who were invited to a Space.
    invited_user_ids: typing.List[UserId]

    # Denotes if the Space is a ticketed Space.
    is_ticketed: bool

    # The language of the Space.
    lang: str

    # The number of participants in a Space.
    participant_count: int

    # A date time stamp for when a Space is scheduled to begin.
    scheduled_start: datetime

    # An array of user ids for people who were speakers in a Space.
    speaker_ids: typing.List[UserId]

    # When the Space was started as a date string.
    started_at: datetime

    # The number of people who have either purchased a ticket or set a reminder for this Space.
    subscriber_count: int

    topics: SpaceTopics

    # When the Space was last updated.
    updated_at: datetime

class Space(RequiredSpace, OptionalSpace):
    pass
