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

from x_python_sdk.type.poll_id import PollId
from x_python_sdk.type.poll_option import PollOption

class RequiredPoll(TypedDict):
    id: PollId

    options: typing.List[PollOption]

class OptionalPoll(TypedDict, total=False):
    duration_minutes: int

    end_datetime: datetime

    voting_status: str

class Poll(RequiredPoll, OptionalPoll):
    pass
