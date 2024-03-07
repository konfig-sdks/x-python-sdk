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

from x_python_sdk.type.create_message_request import CreateMessageRequest
from x_python_sdk.type.dm_participants import DmParticipants

class RequiredCreateDmConversationRequest(TypedDict):
    # The conversation type that is being created.
    conversation_type: str

    message: CreateMessageRequest

    participant_ids: DmParticipants

class OptionalCreateDmConversationRequest(TypedDict, total=False):
    pass

class CreateDmConversationRequest(RequiredCreateDmConversationRequest, OptionalCreateDmConversationRequest):
    pass
