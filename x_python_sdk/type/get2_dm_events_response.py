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

from x_python_sdk.type.dm_event import DmEvent
from x_python_sdk.type.expansions import Expansions
from x_python_sdk.type.get2_dm_events_response_meta import Get2DmEventsResponseMeta
from x_python_sdk.type.problem import Problem

class RequiredGet2DmEventsResponse(TypedDict):
    pass

class OptionalGet2DmEventsResponse(TypedDict, total=False):
    data: typing.List[DmEvent]

    errors: typing.List[Problem]

    includes: Expansions

    meta: Get2DmEventsResponseMeta

class Get2DmEventsResponse(RequiredGet2DmEventsResponse, OptionalGet2DmEventsResponse):
    pass
