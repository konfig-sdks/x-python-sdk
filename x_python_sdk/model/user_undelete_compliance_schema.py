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


class UserUndeleteComplianceSchema(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "user_undelete",
        }
        
        class properties:
        
            @staticmethod
            def user_undelete() -> typing.Type['UserComplianceSchema']:
                return UserComplianceSchema
            __annotations__ = {
                "user_undelete": user_undelete,
            }
    
    user_undelete: 'UserComplianceSchema'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_undelete"]) -> 'UserComplianceSchema': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["user_undelete", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_undelete"]) -> 'UserComplianceSchema': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["user_undelete", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        user_undelete: 'UserComplianceSchema',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserUndeleteComplianceSchema':
        return super().__new__(
            cls,
            *args,
            user_undelete=user_undelete,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.user_compliance_schema import UserComplianceSchema
