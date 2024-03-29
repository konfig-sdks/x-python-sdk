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


class MentionFields(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Represent the portion of text recognized as a User mention, and its start and end position within the text.
    """


    class MetaOapg:
        required = {
            "username",
        }
        
        class properties:
        
            @staticmethod
            def username() -> typing.Type['UserName']:
                return UserName
        
            @staticmethod
            def id() -> typing.Type['UserId']:
                return UserId
            __annotations__ = {
                "username": username,
                "id": id,
            }
    
    username: 'UserName'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> 'UserName': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'UserId': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["username", "id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> 'UserName': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union['UserId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["username", "id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        username: 'UserName',
        id: typing.Union['UserId', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MentionFields':
        return super().__new__(
            cls,
            *args,
            username=username,
            id=id,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.user_id import UserId
from x_python_sdk.model.user_name import UserName
