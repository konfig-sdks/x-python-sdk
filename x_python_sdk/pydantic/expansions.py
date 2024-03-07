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

from x_python_sdk.pydantic.media import Media
from x_python_sdk.pydantic.place import Place
from x_python_sdk.pydantic.poll import Poll
from x_python_sdk.pydantic.topic import Topic
from x_python_sdk.pydantic.tweet import Tweet
from x_python_sdk.pydantic.user import User

class Expansions(BaseModel):
    media: typing.Optional[typing.List[Media]] = Field(None, alias='media')

    places: typing.Optional[typing.List[Place]] = Field(None, alias='places')

    polls: typing.Optional[typing.List[Poll]] = Field(None, alias='polls')

    topics: typing.Optional[typing.List[Topic]] = Field(None, alias='topics')

    tweets: typing.Optional[typing.List[Tweet]] = Field(None, alias='tweets')

    users: typing.Optional[typing.List[User]] = Field(None, alias='users')
    class Config:
        arbitrary_types_allowed = True
