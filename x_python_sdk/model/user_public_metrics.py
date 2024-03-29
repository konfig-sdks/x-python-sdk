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


class UserPublicMetrics(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A list of metrics for this User.
    """


    class MetaOapg:
        required = {
            "tweet_count",
            "following_count",
            "listed_count",
            "followers_count",
        }
        
        class properties:
            followers_count = schemas.IntSchema
            following_count = schemas.IntSchema
            listed_count = schemas.IntSchema
            tweet_count = schemas.IntSchema
            __annotations__ = {
                "followers_count": followers_count,
                "following_count": following_count,
                "listed_count": listed_count,
                "tweet_count": tweet_count,
            }
    
    tweet_count: MetaOapg.properties.tweet_count
    following_count: MetaOapg.properties.following_count
    listed_count: MetaOapg.properties.listed_count
    followers_count: MetaOapg.properties.followers_count
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["followers_count"]) -> MetaOapg.properties.followers_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["following_count"]) -> MetaOapg.properties.following_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["listed_count"]) -> MetaOapg.properties.listed_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tweet_count"]) -> MetaOapg.properties.tweet_count: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["followers_count", "following_count", "listed_count", "tweet_count", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["followers_count"]) -> MetaOapg.properties.followers_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["following_count"]) -> MetaOapg.properties.following_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["listed_count"]) -> MetaOapg.properties.listed_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tweet_count"]) -> MetaOapg.properties.tweet_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["followers_count", "following_count", "listed_count", "tweet_count", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tweet_count: typing.Union[MetaOapg.properties.tweet_count, decimal.Decimal, int, ],
        following_count: typing.Union[MetaOapg.properties.following_count, decimal.Decimal, int, ],
        listed_count: typing.Union[MetaOapg.properties.listed_count, decimal.Decimal, int, ],
        followers_count: typing.Union[MetaOapg.properties.followers_count, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserPublicMetrics':
        return super().__new__(
            cls,
            *args,
            tweet_count=tweet_count,
            following_count=following_count,
            listed_count=listed_count,
            followers_count=followers_count,
            _configuration=_configuration,
            **kwargs,
        )
