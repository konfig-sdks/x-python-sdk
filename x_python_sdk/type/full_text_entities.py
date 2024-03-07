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

from x_python_sdk.type.cashtag_entity import CashtagEntity
from x_python_sdk.type.full_text_entities_annotations import FullTextEntitiesAnnotations
from x_python_sdk.type.hashtag_entity import HashtagEntity
from x_python_sdk.type.mention_entity import MentionEntity
from x_python_sdk.type.url_entity import UrlEntity

class RequiredFullTextEntities(TypedDict):
    pass

class OptionalFullTextEntities(TypedDict, total=False):
    annotations: FullTextEntitiesAnnotations

    cashtags: typing.List[CashtagEntity]

    hashtags: typing.List[HashtagEntity]

    mentions: typing.List[MentionEntity]

    urls: typing.List[UrlEntity]

class FullTextEntities(RequiredFullTextEntities, OptionalFullTextEntities):
    pass
