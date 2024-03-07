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


class ModelList(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A Twitter List is a curated group of accounts.
    """


    class MetaOapg:
        required = {
            "name",
            "id",
        }
        
        class properties:
        
            @staticmethod
            def id() -> typing.Type['ListId']:
                return ListId
            name = schemas.StrSchema
            description = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            follower_count = schemas.IntSchema
            member_count = schemas.IntSchema
        
            @staticmethod
            def owner_id() -> typing.Type['UserId']:
                return UserId
            private = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "description": description,
                "created_at": created_at,
                "follower_count": follower_count,
                "member_count": member_count,
                "owner_id": owner_id,
                "private": private,
            }
    
    name: MetaOapg.properties.name
    id: 'ListId'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'ListId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["follower_count"]) -> MetaOapg.properties.follower_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["member_count"]) -> MetaOapg.properties.member_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner_id"]) -> 'UserId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["private"]) -> MetaOapg.properties.private: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "description", "created_at", "follower_count", "member_count", "owner_id", "private", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'ListId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["follower_count"]) -> typing.Union[MetaOapg.properties.follower_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["member_count"]) -> typing.Union[MetaOapg.properties.member_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner_id"]) -> typing.Union['UserId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["private"]) -> typing.Union[MetaOapg.properties.private, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "description", "created_at", "follower_count", "member_count", "owner_id", "private", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: 'ListId',
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        follower_count: typing.Union[MetaOapg.properties.follower_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        member_count: typing.Union[MetaOapg.properties.member_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        owner_id: typing.Union['UserId', schemas.Unset] = schemas.unset,
        private: typing.Union[MetaOapg.properties.private, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelList':
        return super().__new__(
            cls,
            *args,
            name=name,
            id=id,
            description=description,
            created_at=created_at,
            follower_count=follower_count,
            member_count=member_count,
            owner_id=owner_id,
            private=private,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.list_id import ListId
from x_python_sdk.model.user_id import UserId
