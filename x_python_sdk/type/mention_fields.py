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

from x_python_sdk.type.user_id import UserId
from x_python_sdk.type.user_name import UserName

class RequiredMentionFields(TypedDict):
    username: UserName

class OptionalMentionFields(TypedDict, total=False):
    id: UserId

class MentionFields(RequiredMentionFields, OptionalMentionFields):
    pass
