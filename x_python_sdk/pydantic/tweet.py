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

from x_python_sdk.pydantic.context_annotation import ContextAnnotation
from x_python_sdk.pydantic.full_text_entities import FullTextEntities
from x_python_sdk.pydantic.reply_settings import ReplySettings
from x_python_sdk.pydantic.tweet_attachments import TweetAttachments
from x_python_sdk.pydantic.tweet_edit_controls import TweetEditControls
from x_python_sdk.pydantic.tweet_geo import TweetGeo
from x_python_sdk.pydantic.tweet_id import TweetId
from x_python_sdk.pydantic.tweet_non_public_metrics import TweetNonPublicMetrics
from x_python_sdk.pydantic.tweet_organic_metrics import TweetOrganicMetrics
from x_python_sdk.pydantic.tweet_promoted_metrics import TweetPromotedMetrics
from x_python_sdk.pydantic.tweet_public_metrics import TweetPublicMetrics
from x_python_sdk.pydantic.tweet_referenced_tweets import TweetReferencedTweets
from x_python_sdk.pydantic.tweet_withheld import TweetWithheld
from x_python_sdk.pydantic.user_id import UserId

class Tweet(BaseModel):
    # A list of Tweet Ids in this Tweet chain.
    edit_history_tweet_ids: typing.List[TweetId] = Field(alias='edit_history_tweet_ids')

    id: TweetId = Field(alias='id')

    # The content of the Tweet.
    text: str = Field(alias='text')

    attachments: typing.Optional[TweetAttachments] = Field(None, alias='attachments')

    author_id: typing.Optional[UserId] = Field(None, alias='author_id')

    context_annotations: typing.Optional[typing.List[ContextAnnotation]] = Field(None, alias='context_annotations')

    conversation_id: typing.Optional[TweetId] = Field(None, alias='conversation_id')

    # Creation time of the Tweet.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    edit_controls: typing.Optional[TweetEditControls] = Field(None, alias='edit_controls')

    entities: typing.Optional[FullTextEntities] = Field(None, alias='entities')

    geo: typing.Optional[TweetGeo] = Field(None, alias='geo')

    in_reply_to_user_id: typing.Optional[UserId] = Field(None, alias='in_reply_to_user_id')

    # Language of the Tweet, if detected by Twitter. Returned as a BCP47 language tag.
    lang: typing.Optional[str] = Field(None, alias='lang')

    non_public_metrics: typing.Optional[TweetNonPublicMetrics] = Field(None, alias='non_public_metrics')

    organic_metrics: typing.Optional[TweetOrganicMetrics] = Field(None, alias='organic_metrics')

    # Indicates if this Tweet contains URLs marked as sensitive, for example content suitable for mature audiences.
    possibly_sensitive: typing.Optional[bool] = Field(None, alias='possibly_sensitive')

    promoted_metrics: typing.Optional[TweetPromotedMetrics] = Field(None, alias='promoted_metrics')

    public_metrics: typing.Optional[TweetPublicMetrics] = Field(None, alias='public_metrics')

    referenced_tweets: typing.Optional[TweetReferencedTweets] = Field(None, alias='referenced_tweets')

    reply_settings: typing.Optional[ReplySettings] = Field(None, alias='reply_settings')

    # This is deprecated.
    source: typing.Optional[str] = Field(None, alias='source')

    withheld: typing.Optional[TweetWithheld] = Field(None, alias='withheld')
    class Config:
        arbitrary_types_allowed = True
