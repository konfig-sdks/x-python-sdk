# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.62
    Created by: https://developer.twitter.com/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from x_python_sdk import schemas  # noqa: F401


class TweetReferencedTweets(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    A list of Tweets this Tweet refers to. For example, if the parent Tweet is a Retweet, a Quoted Tweet or a Reply, it will include the related Tweet referenced to by its parent.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['TweetReferencedTweetsItem']:
            return TweetReferencedTweetsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['TweetReferencedTweetsItem'], typing.List['TweetReferencedTweetsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TweetReferencedTweets':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'TweetReferencedTweetsItem':
        return super().__getitem__(i)

from x_python_sdk.model.tweet_referenced_tweets_item import TweetReferencedTweetsItem
