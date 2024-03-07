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

from x_python_sdk.type.dm_event_attachments_card_ids import DmEventAttachmentsCardIds
from x_python_sdk.type.media_key import MediaKey

class RequiredDmEventAttachments(TypedDict):
    pass

class OptionalDmEventAttachments(TypedDict, total=False):
    card_ids: DmEventAttachmentsCardIds

    # A list of Media Keys for each one of the media attachments (if media are attached).
    media_keys: typing.List[MediaKey]

class DmEventAttachments(RequiredDmEventAttachments, OptionalDmEventAttachments):
    pass
