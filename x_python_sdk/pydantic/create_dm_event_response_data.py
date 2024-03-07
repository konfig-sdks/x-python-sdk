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

from x_python_sdk.pydantic.dm_conversation_id import DmConversationId
from x_python_sdk.pydantic.dm_event_id import DmEventId

class CreateDmEventResponseData(BaseModel):
    dm_conversation_id: DmConversationId = Field(alias='dm_conversation_id')

    dm_event_id: DmEventId = Field(alias='dm_event_id')
    class Config:
        arbitrary_types_allowed = True
