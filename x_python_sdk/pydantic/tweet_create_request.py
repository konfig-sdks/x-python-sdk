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

from x_python_sdk.pydantic.tweet_create_request_geo import TweetCreateRequestGeo
from x_python_sdk.pydantic.tweet_create_request_media import TweetCreateRequestMedia
from x_python_sdk.pydantic.tweet_create_request_poll import TweetCreateRequestPoll
from x_python_sdk.pydantic.tweet_create_request_reply import TweetCreateRequestReply
from x_python_sdk.pydantic.tweet_id import TweetId

class TweetCreateRequest(BaseModel):
    # Card Uri Parameter. This is mutually exclusive from Quote Tweet Id, Poll, Media, and Direct Message Deep Link.
    card_uri: typing.Optional[str] = Field(None, alias='card_uri')

    # Link to take the conversation from the public timeline to a private Direct Message.
    direct_message_deep_link: typing.Optional[str] = Field(None, alias='direct_message_deep_link')

    # Exclusive Tweet for super followers.
    for_super_followers_only: typing.Optional[bool] = Field(None, alias='for_super_followers_only')

    geo: typing.Optional[TweetCreateRequestGeo] = Field(None, alias='geo')

    media: typing.Optional[TweetCreateRequestMedia] = Field(None, alias='media')

    # Nullcasted (promoted-only) Tweets do not appear in the public timeline and are not served to followers.
    nullcast: typing.Optional[bool] = Field(None, alias='nullcast')

    poll: typing.Optional[TweetCreateRequestPoll] = Field(None, alias='poll')

    quote_tweet_id: typing.Optional[TweetId] = Field(None, alias='quote_tweet_id')

    reply: typing.Optional[TweetCreateRequestReply] = Field(None, alias='reply')

    # Settings to indicate who can reply to the Tweet.
    reply_settings: typing.Optional[Literal["following", "mentionedUsers"]] = Field(None, alias='reply_settings')

    # The content of the Tweet.
    text: typing.Optional[str] = Field(None, alias='text')
    class Config:
        arbitrary_types_allowed = True
