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


class UserProfileModificationObjectSchema(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "event_at",
            "user",
            "new_value",
            "profile_field",
        }
        
        class properties:
            event_at = schemas.DateTimeSchema
            new_value = schemas.StrSchema
            profile_field = schemas.StrSchema
        
            @staticmethod
            def user() -> typing.Type['UserProfileModificationObjectSchemaUser']:
                return UserProfileModificationObjectSchemaUser
            __annotations__ = {
                "event_at": event_at,
                "new_value": new_value,
                "profile_field": profile_field,
                "user": user,
            }
    
    event_at: MetaOapg.properties.event_at
    user: 'UserProfileModificationObjectSchemaUser'
    new_value: MetaOapg.properties.new_value
    profile_field: MetaOapg.properties.profile_field
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_at"]) -> MetaOapg.properties.event_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["new_value"]) -> MetaOapg.properties.new_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profile_field"]) -> MetaOapg.properties.profile_field: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'UserProfileModificationObjectSchemaUser': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["event_at", "new_value", "profile_field", "user", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_at"]) -> MetaOapg.properties.event_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["new_value"]) -> MetaOapg.properties.new_value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profile_field"]) -> MetaOapg.properties.profile_field: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> 'UserProfileModificationObjectSchemaUser': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["event_at", "new_value", "profile_field", "user", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        event_at: typing.Union[MetaOapg.properties.event_at, str, datetime, ],
        user: 'UserProfileModificationObjectSchemaUser',
        new_value: typing.Union[MetaOapg.properties.new_value, str, ],
        profile_field: typing.Union[MetaOapg.properties.profile_field, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserProfileModificationObjectSchema':
        return super().__new__(
            cls,
            *args,
            event_at=event_at,
            user=user,
            new_value=new_value,
            profile_field=profile_field,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.user_profile_modification_object_schema_user import UserProfileModificationObjectSchemaUser
