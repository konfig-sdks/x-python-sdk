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

from x_python_sdk.type.dm_conversation_id import DmConversationId
from x_python_sdk.type.dm_event_id import DmEventId

class RequiredCreateDmEventResponseData(TypedDict):
    dm_conversation_id: DmConversationId

    dm_event_id: DmEventId

class OptionalCreateDmEventResponseData(TypedDict, total=False):
    pass

class CreateDmEventResponseData(RequiredCreateDmEventResponseData, OptionalCreateDmEventResponseData):
    pass
