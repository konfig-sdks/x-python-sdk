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


class TweetUnviewableTweet(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "id",
            "author_id",
        }
        
        class properties:
        
            @staticmethod
            def author_id() -> typing.Type['UserId']:
                return UserId
        
            @staticmethod
            def id() -> typing.Type['TweetId']:
                return TweetId
            __annotations__ = {
                "author_id": author_id,
                "id": id,
            }
    
    id: 'TweetId'
    author_id: 'UserId'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["author_id"]) -> 'UserId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'TweetId': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["author_id", "id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["author_id"]) -> 'UserId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'TweetId': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["author_id", "id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: 'TweetId',
        author_id: 'UserId',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TweetUnviewableTweet':
        return super().__new__(
            cls,
            *args,
            id=id,
            author_id=author_id,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.tweet_id import TweetId
from x_python_sdk.model.user_id import UserId
