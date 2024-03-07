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


class CreateDmConversationRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "conversation_type",
            "participant_ids",
            "message",
        }
        
        class properties:
            
            
            class conversation_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def GROUP(cls):
                    return cls("Group")
        
            @staticmethod
            def message() -> typing.Type['CreateMessageRequest']:
                return CreateMessageRequest
        
            @staticmethod
            def participant_ids() -> typing.Type['DmParticipants']:
                return DmParticipants
            __annotations__ = {
                "conversation_type": conversation_type,
                "message": message,
                "participant_ids": participant_ids,
            }
    
    conversation_type: MetaOapg.properties.conversation_type
    participant_ids: 'DmParticipants'
    message: 'CreateMessageRequest'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conversation_type"]) -> MetaOapg.properties.conversation_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> 'CreateMessageRequest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["participant_ids"]) -> 'DmParticipants': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["conversation_type", "message", "participant_ids", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conversation_type"]) -> MetaOapg.properties.conversation_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> 'CreateMessageRequest': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["participant_ids"]) -> 'DmParticipants': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["conversation_type", "message", "participant_ids", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        conversation_type: typing.Union[MetaOapg.properties.conversation_type, str, ],
        participant_ids: 'DmParticipants',
        message: 'CreateMessageRequest',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateDmConversationRequest':
        return super().__new__(
            cls,
            *args,
            conversation_type=conversation_type,
            participant_ids=participant_ids,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.create_message_request import CreateMessageRequest
from x_python_sdk.model.dm_participants import DmParticipants