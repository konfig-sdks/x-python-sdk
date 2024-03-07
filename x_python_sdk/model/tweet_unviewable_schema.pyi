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


class TweetUnviewableSchema(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "public_tweet_unviewable",
        }
        
        class properties:
        
            @staticmethod
            def public_tweet_unviewable() -> typing.Type['TweetUnviewable']:
                return TweetUnviewable
            __annotations__ = {
                "public_tweet_unviewable": public_tweet_unviewable,
            }
    
    public_tweet_unviewable: 'TweetUnviewable'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["public_tweet_unviewable"]) -> 'TweetUnviewable': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["public_tweet_unviewable", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["public_tweet_unviewable"]) -> 'TweetUnviewable': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["public_tweet_unviewable", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        public_tweet_unviewable: 'TweetUnviewable',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TweetUnviewableSchema':
        return super().__new__(
            cls,
            *args,
            public_tweet_unviewable=public_tweet_unviewable,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.tweet_unviewable import TweetUnviewable