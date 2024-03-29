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


class TweetCreateRequestMedia(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Media information being attached to created Tweet. This is mutually exclusive from Quote Tweet Id, Poll, and Card URI.
    """


    class MetaOapg:
        required = {
            "media_ids",
        }
        
        class properties:
            
            
            class media_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MediaId']:
                        return MediaId
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['MediaId'], typing.List['MediaId']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'media_ids':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MediaId':
                    return super().__getitem__(i)
            
            
            class tagged_user_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['UserId']:
                        return UserId
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['UserId'], typing.List['UserId']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tagged_user_ids':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'UserId':
                    return super().__getitem__(i)
            __annotations__ = {
                "media_ids": media_ids,
                "tagged_user_ids": tagged_user_ids,
            }
    
    media_ids: MetaOapg.properties.media_ids
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["media_ids"]) -> MetaOapg.properties.media_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tagged_user_ids"]) -> MetaOapg.properties.tagged_user_ids: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["media_ids", "tagged_user_ids", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["media_ids"]) -> MetaOapg.properties.media_ids: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tagged_user_ids"]) -> typing.Union[MetaOapg.properties.tagged_user_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["media_ids", "tagged_user_ids", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        media_ids: typing.Union[MetaOapg.properties.media_ids, list, tuple, ],
        tagged_user_ids: typing.Union[MetaOapg.properties.tagged_user_ids, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TweetCreateRequestMedia':
        return super().__new__(
            cls,
            *args,
            media_ids=media_ids,
            tagged_user_ids=tagged_user_ids,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.media_id import MediaId
from x_python_sdk.model.user_id import UserId
