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

from x_python_sdk.type.tweet_create_request_geo import TweetCreateRequestGeo
from x_python_sdk.type.tweet_create_request_media import TweetCreateRequestMedia
from x_python_sdk.type.tweet_create_request_poll import TweetCreateRequestPoll
from x_python_sdk.type.tweet_create_request_reply import TweetCreateRequestReply
from x_python_sdk.type.tweet_id import TweetId

class RequiredTweetCreateRequest(TypedDict):
    pass

class OptionalTweetCreateRequest(TypedDict, total=False):
    # Card Uri Parameter. This is mutually exclusive from Quote Tweet Id, Poll, Media, and Direct Message Deep Link.
    card_uri: str

    # Link to take the conversation from the public timeline to a private Direct Message.
    direct_message_deep_link: str

    # Exclusive Tweet for super followers.
    for_super_followers_only: bool

    geo: TweetCreateRequestGeo

    media: TweetCreateRequestMedia

    # Nullcasted (promoted-only) Tweets do not appear in the public timeline and are not served to followers.
    nullcast: bool

    poll: TweetCreateRequestPoll

    quote_tweet_id: TweetId

    reply: TweetCreateRequestReply

    # Settings to indicate who can reply to the Tweet.
    reply_settings: str

    # The content of the Tweet.
    text: str

class TweetCreateRequest(RequiredTweetCreateRequest, OptionalTweetCreateRequest):
    pass
