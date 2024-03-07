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

from x_python_sdk.pydantic.user_profile_modification_object_schema_user import UserProfileModificationObjectSchemaUser

class UserProfileModificationObjectSchema(BaseModel):
    # Event time.
    event_at: datetime = Field(alias='event_at')

    new_value: str = Field(alias='new_value')

    profile_field: str = Field(alias='profile_field')

    user: UserProfileModificationObjectSchemaUser = Field(alias='user')
    class Config:
        arbitrary_types_allowed = True
