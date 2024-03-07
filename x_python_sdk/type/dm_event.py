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
from x_python_sdk.type.dm_event_attachments import DmEventAttachments
from x_python_sdk.type.dm_event_id import DmEventId
from x_python_sdk.type.dm_event_referenced_tweets import DmEventReferencedTweets
from x_python_sdk.type.user_id import UserId

class RequiredDmEvent(TypedDict):
    event_type: str

    id: DmEventId

class OptionalDmEvent(TypedDict, total=False):
    attachments: DmEventAttachments

    created_at: datetime

    dm_conversation_id: DmConversationId

    # A list of participants for a ParticipantsJoin or ParticipantsLeave event_type.
    participant_ids: typing.List[UserId]

    referenced_tweets: DmEventReferencedTweets

    sender_id: UserId

    text: str

class DmEvent(RequiredDmEvent, OptionalDmEvent):
    pass
