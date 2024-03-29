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


class TweetCreateRequestPoll(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Poll options for a Tweet with a poll. This is mutually exclusive from Media, Quote Tweet Id, and Card URI.
    """


    class MetaOapg:
        required = {
            "duration_minutes",
            "options",
        }
        
        class properties:
            
            
            class duration_minutes(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 10080
                    inclusive_minimum = 5
        
            @staticmethod
            def options() -> typing.Type['TweetCreateRequestPollOptions']:
                return TweetCreateRequestPollOptions
            
            
            class reply_settings(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "following": "FOLLOWING",
                        "mentionedUsers": "MENTIONED_USERS",
                    }
                
                @schemas.classproperty
                def FOLLOWING(cls):
                    return cls("following")
                
                @schemas.classproperty
                def MENTIONED_USERS(cls):
                    return cls("mentionedUsers")
            __annotations__ = {
                "duration_minutes": duration_minutes,
                "options": options,
                "reply_settings": reply_settings,
            }
    
    duration_minutes: MetaOapg.properties.duration_minutes
    options: 'TweetCreateRequestPollOptions'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration_minutes"]) -> MetaOapg.properties.duration_minutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> 'TweetCreateRequestPollOptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reply_settings"]) -> MetaOapg.properties.reply_settings: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["duration_minutes", "options", "reply_settings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration_minutes"]) -> MetaOapg.properties.duration_minutes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> 'TweetCreateRequestPollOptions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reply_settings"]) -> typing.Union[MetaOapg.properties.reply_settings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["duration_minutes", "options", "reply_settings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        duration_minutes: typing.Union[MetaOapg.properties.duration_minutes, decimal.Decimal, int, ],
        options: 'TweetCreateRequestPollOptions',
        reply_settings: typing.Union[MetaOapg.properties.reply_settings, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TweetCreateRequestPoll':
        return super().__new__(
            cls,
            *args,
            duration_minutes=duration_minutes,
            options=options,
            reply_settings=reply_settings,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.tweet_create_request_poll_options import TweetCreateRequestPollOptions
