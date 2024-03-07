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
from x_python_sdk.pydantic.dm_event_attachments import DmEventAttachments
from x_python_sdk.pydantic.dm_event_id import DmEventId
from x_python_sdk.pydantic.dm_event_referenced_tweets import DmEventReferencedTweets
from x_python_sdk.pydantic.user_id import UserId

class DmEvent(BaseModel):
    event_type: str = Field(alias='event_type')

    id: DmEventId = Field(alias='id')

    attachments: typing.Optional[DmEventAttachments] = Field(None, alias='attachments')

    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    dm_conversation_id: typing.Optional[DmConversationId] = Field(None, alias='dm_conversation_id')

    # A list of participants for a ParticipantsJoin or ParticipantsLeave event_type.
    participant_ids: typing.Optional[typing.List[UserId]] = Field(None, alias='participant_ids')

    referenced_tweets: typing.Optional[DmEventReferencedTweets] = Field(None, alias='referenced_tweets')

    sender_id: typing.Optional[UserId] = Field(None, alias='sender_id')

    text: typing.Optional[str] = Field(None, alias='text')
    class Config:
        arbitrary_types_allowed = True
