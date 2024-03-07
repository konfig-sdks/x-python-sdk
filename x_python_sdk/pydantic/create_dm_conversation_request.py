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

from x_python_sdk.pydantic.create_message_request import CreateMessageRequest
from x_python_sdk.pydantic.dm_participants import DmParticipants

class CreateDmConversationRequest(BaseModel):
    # The conversation type that is being created.
    conversation_type: Literal["Group"] = Field(alias='conversation_type')

    message: CreateMessageRequest = Field(alias='message')

    participant_ids: DmParticipants = Field(alias='participant_ids')
    class Config:
        arbitrary_types_allowed = True
