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


class DmEventAttachments(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Specifies the type of attachments (if any) present in this DM.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def card_ids() -> typing.Type['DmEventAttachmentsCardIds']:
                return DmEventAttachmentsCardIds
            
            
            class media_keys(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MediaKey']:
                        return MediaKey
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['MediaKey'], typing.List['MediaKey']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'media_keys':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MediaKey':
                    return super().__getitem__(i)
            __annotations__ = {
                "card_ids": card_ids,
                "media_keys": media_keys,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["card_ids"]) -> 'DmEventAttachmentsCardIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["media_keys"]) -> MetaOapg.properties.media_keys: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["card_ids", "media_keys", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["card_ids"]) -> typing.Union['DmEventAttachmentsCardIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["media_keys"]) -> typing.Union[MetaOapg.properties.media_keys, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["card_ids", "media_keys", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        card_ids: typing.Union['DmEventAttachmentsCardIds', schemas.Unset] = schemas.unset,
        media_keys: typing.Union[MetaOapg.properties.media_keys, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DmEventAttachments':
        return super().__new__(
            cls,
            *args,
            card_ids=card_ids,
            media_keys=media_keys,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.dm_event_attachments_card_ids import DmEventAttachmentsCardIds
from x_python_sdk.model.media_key import MediaKey
