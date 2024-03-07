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


class DmEvent(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "event_type",
            "id",
        }
        
        class properties:
            event_type = schemas.StrSchema
        
            @staticmethod
            def id() -> typing.Type['DmEventId']:
                return DmEventId
        
            @staticmethod
            def attachments() -> typing.Type['DmEventAttachments']:
                return DmEventAttachments
            created_at = schemas.DateTimeSchema
        
            @staticmethod
            def dm_conversation_id() -> typing.Type['DmConversationId']:
                return DmConversationId
            
            
            class participant_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    min_items = 1
                    
                    @staticmethod
                    def items() -> typing.Type['UserId']:
                        return UserId
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['UserId'], typing.List['UserId']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'participant_ids':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'UserId':
                    return super().__getitem__(i)
        
            @staticmethod
            def referenced_tweets() -> typing.Type['DmEventReferencedTweets']:
                return DmEventReferencedTweets
        
            @staticmethod
            def sender_id() -> typing.Type['UserId']:
                return UserId
            text = schemas.StrSchema
            __annotations__ = {
                "event_type": event_type,
                "id": id,
                "attachments": attachments,
                "created_at": created_at,
                "dm_conversation_id": dm_conversation_id,
                "participant_ids": participant_ids,
                "referenced_tweets": referenced_tweets,
                "sender_id": sender_id,
                "text": text,
            }
    
    event_type: MetaOapg.properties.event_type
    id: 'DmEventId'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_type"]) -> MetaOapg.properties.event_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'DmEventId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachments"]) -> 'DmEventAttachments': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dm_conversation_id"]) -> 'DmConversationId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["participant_ids"]) -> MetaOapg.properties.participant_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referenced_tweets"]) -> 'DmEventReferencedTweets': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sender_id"]) -> 'UserId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["event_type", "id", "attachments", "created_at", "dm_conversation_id", "participant_ids", "referenced_tweets", "sender_id", "text", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_type"]) -> MetaOapg.properties.event_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'DmEventId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachments"]) -> typing.Union['DmEventAttachments', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dm_conversation_id"]) -> typing.Union['DmConversationId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["participant_ids"]) -> typing.Union[MetaOapg.properties.participant_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referenced_tweets"]) -> typing.Union['DmEventReferencedTweets', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sender_id"]) -> typing.Union['UserId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> typing.Union[MetaOapg.properties.text, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["event_type", "id", "attachments", "created_at", "dm_conversation_id", "participant_ids", "referenced_tweets", "sender_id", "text", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        event_type: typing.Union[MetaOapg.properties.event_type, str, ],
        id: 'DmEventId',
        attachments: typing.Union['DmEventAttachments', schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        dm_conversation_id: typing.Union['DmConversationId', schemas.Unset] = schemas.unset,
        participant_ids: typing.Union[MetaOapg.properties.participant_ids, list, tuple, schemas.Unset] = schemas.unset,
        referenced_tweets: typing.Union['DmEventReferencedTweets', schemas.Unset] = schemas.unset,
        sender_id: typing.Union['UserId', schemas.Unset] = schemas.unset,
        text: typing.Union[MetaOapg.properties.text, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DmEvent':
        return super().__new__(
            cls,
            *args,
            event_type=event_type,
            id=id,
            attachments=attachments,
            created_at=created_at,
            dm_conversation_id=dm_conversation_id,
            participant_ids=participant_ids,
            referenced_tweets=referenced_tweets,
            sender_id=sender_id,
            text=text,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.dm_conversation_id import DmConversationId
from x_python_sdk.model.dm_event_attachments import DmEventAttachments
from x_python_sdk.model.dm_event_id import DmEventId
from x_python_sdk.model.dm_event_referenced_tweets import DmEventReferencedTweets
from x_python_sdk.model.user_id import UserId
