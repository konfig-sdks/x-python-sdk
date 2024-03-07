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


class Get2SpacesIdBuyersResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class data(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['User']:
                        return User
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['User'], typing.List['User']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'data':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'User':
                    return super().__getitem__(i)
            
            
            class errors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Problem']:
                        return Problem
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Problem'], typing.List['Problem']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'errors':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Problem':
                    return super().__getitem__(i)
        
            @staticmethod
            def includes() -> typing.Type['Expansions']:
                return Expansions
        
            @staticmethod
            def meta() -> typing.Type['Get2SpacesIdBuyersResponseMeta']:
                return Get2SpacesIdBuyersResponseMeta
            __annotations__ = {
                "data": data,
                "errors": errors,
                "includes": includes,
                "meta": meta,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includes"]) -> 'Expansions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'Get2SpacesIdBuyersResponseMeta': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "errors", "includes", "meta", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> typing.Union[MetaOapg.properties.errors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includes"]) -> typing.Union['Expansions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['Get2SpacesIdBuyersResponseMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "errors", "includes", "meta", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union[MetaOapg.properties.data, list, tuple, schemas.Unset] = schemas.unset,
        errors: typing.Union[MetaOapg.properties.errors, list, tuple, schemas.Unset] = schemas.unset,
        includes: typing.Union['Expansions', schemas.Unset] = schemas.unset,
        meta: typing.Union['Get2SpacesIdBuyersResponseMeta', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Get2SpacesIdBuyersResponse':
        return super().__new__(
            cls,
            *args,
            data=data,
            errors=errors,
            includes=includes,
            meta=meta,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.expansions import Expansions
from x_python_sdk.model.get2_spaces_id_buyers_response_meta import Get2SpacesIdBuyersResponseMeta
from x_python_sdk.model.problem import Problem
from x_python_sdk.model.user import User
