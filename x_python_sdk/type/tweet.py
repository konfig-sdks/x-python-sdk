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

from x_python_sdk.type.context_annotation import ContextAnnotation
from x_python_sdk.type.full_text_entities import FullTextEntities
from x_python_sdk.type.reply_settings import ReplySettings
from x_python_sdk.type.tweet_attachments import TweetAttachments
from x_python_sdk.type.tweet_edit_controls import TweetEditControls
from x_python_sdk.type.tweet_geo import TweetGeo
from x_python_sdk.type.tweet_id import TweetId
from x_python_sdk.type.tweet_non_public_metrics import TweetNonPublicMetrics
from x_python_sdk.type.tweet_organic_metrics import TweetOrganicMetrics
from x_python_sdk.type.tweet_promoted_metrics import TweetPromotedMetrics
from x_python_sdk.type.tweet_public_metrics import TweetPublicMetrics
from x_python_sdk.type.tweet_referenced_tweets import TweetReferencedTweets
from x_python_sdk.type.tweet_withheld import TweetWithheld
from x_python_sdk.type.user_id import UserId

class RequiredTweet(TypedDict):
    # A list of Tweet Ids in this Tweet chain.
    edit_history_tweet_ids: typing.List[TweetId]

    id: TweetId

    # The content of the Tweet.
    text: str

class OptionalTweet(TypedDict, total=False):
    attachments: TweetAttachments

    author_id: UserId

    context_annotations: typing.List[ContextAnnotation]

    conversation_id: TweetId

    # Creation time of the Tweet.
    created_at: datetime

    edit_controls: TweetEditControls

    entities: FullTextEntities

    geo: TweetGeo

    in_reply_to_user_id: UserId

    # Language of the Tweet, if detected by Twitter. Returned as a BCP47 language tag.
    lang: str

    non_public_metrics: TweetNonPublicMetrics

    organic_metrics: TweetOrganicMetrics

    # Indicates if this Tweet contains URLs marked as sensitive, for example content suitable for mature audiences.
    possibly_sensitive: bool

    promoted_metrics: TweetPromotedMetrics

    public_metrics: TweetPublicMetrics

    referenced_tweets: TweetReferencedTweets

    reply_settings: ReplySettings

    # This is deprecated.
    source: str

    withheld: TweetWithheld

class Tweet(RequiredTweet, OptionalTweet):
    pass
