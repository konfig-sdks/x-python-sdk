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


class Get2SpacesIdTweetsResponseMeta(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def next_token() -> typing.Type['NextToken']:
                return NextToken
        
            @staticmethod
            def previous_token() -> typing.Type['PreviousToken']:
                return PreviousToken
            result_count = schemas.Int32Schema
            __annotations__ = {
                "next_token": next_token,
                "previous_token": previous_token,
                "result_count": result_count,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_token"]) -> 'NextToken': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["previous_token"]) -> 'PreviousToken': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result_count"]) -> MetaOapg.properties.result_count: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["next_token", "previous_token", "result_count", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_token"]) -> typing.Union['NextToken', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["previous_token"]) -> typing.Union['PreviousToken', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result_count"]) -> typing.Union[MetaOapg.properties.result_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["next_token", "previous_token", "result_count", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        next_token: typing.Union['NextToken', schemas.Unset] = schemas.unset,
        previous_token: typing.Union['PreviousToken', schemas.Unset] = schemas.unset,
        result_count: typing.Union[MetaOapg.properties.result_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Get2SpacesIdTweetsResponseMeta':
        return super().__new__(
            cls,
            *args,
            next_token=next_token,
            previous_token=previous_token,
            result_count=result_count,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.next_token import NextToken
from x_python_sdk.model.previous_token import PreviousToken
