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


class UserEntities(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A list of metadata found in the User's profile description.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def description() -> typing.Type['FullTextEntities']:
                return FullTextEntities
        
            @staticmethod
            def url() -> typing.Type['UserEntitiesUrl']:
                return UserEntitiesUrl
            __annotations__ = {
                "description": description,
                "url": url,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> 'FullTextEntities': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> 'UserEntitiesUrl': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union['FullTextEntities', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union['UserEntitiesUrl', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union['FullTextEntities', schemas.Unset] = schemas.unset,
        url: typing.Union['UserEntitiesUrl', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserEntities':
        return super().__new__(
            cls,
            *args,
            description=description,
            url=url,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.full_text_entities import FullTextEntities
from x_python_sdk.model.user_entities_url import UserEntitiesUrl