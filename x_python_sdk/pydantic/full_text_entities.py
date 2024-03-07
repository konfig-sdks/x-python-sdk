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

from x_python_sdk.pydantic.cashtag_entity import CashtagEntity
from x_python_sdk.pydantic.full_text_entities_annotations import FullTextEntitiesAnnotations
from x_python_sdk.pydantic.hashtag_entity import HashtagEntity
from x_python_sdk.pydantic.mention_entity import MentionEntity
from x_python_sdk.pydantic.url_entity import UrlEntity

class FullTextEntities(BaseModel):
    annotations: typing.Optional[FullTextEntitiesAnnotations] = Field(None, alias='annotations')

    cashtags: typing.Optional[typing.List[CashtagEntity]] = Field(None, alias='cashtags')

    hashtags: typing.Optional[typing.List[HashtagEntity]] = Field(None, alias='hashtags')

    mentions: typing.Optional[typing.List[MentionEntity]] = Field(None, alias='mentions')

    urls: typing.Optional[typing.List[UrlEntity]] = Field(None, alias='urls')
    class Config:
        arbitrary_types_allowed = True
