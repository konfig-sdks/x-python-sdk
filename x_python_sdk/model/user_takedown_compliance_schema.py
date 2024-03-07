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


class UserTakedownComplianceSchema(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "withheld_in_countries",
            "event_at",
            "user",
        }
        
        class properties:
            event_at = schemas.DateTimeSchema
        
            @staticmethod
            def user() -> typing.Type['UserTakedownComplianceSchemaUser']:
                return UserTakedownComplianceSchemaUser
            
            
            class withheld_in_countries(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    min_items = 1
                    
                    @staticmethod
                    def items() -> typing.Type['CountryCode']:
                        return CountryCode
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CountryCode'], typing.List['CountryCode']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'withheld_in_countries':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CountryCode':
                    return super().__getitem__(i)
            __annotations__ = {
                "event_at": event_at,
                "user": user,
                "withheld_in_countries": withheld_in_countries,
            }
    
    withheld_in_countries: MetaOapg.properties.withheld_in_countries
    event_at: MetaOapg.properties.event_at
    user: 'UserTakedownComplianceSchemaUser'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_at"]) -> MetaOapg.properties.event_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'UserTakedownComplianceSchemaUser': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["withheld_in_countries"]) -> MetaOapg.properties.withheld_in_countries: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["event_at", "user", "withheld_in_countries", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_at"]) -> MetaOapg.properties.event_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> 'UserTakedownComplianceSchemaUser': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["withheld_in_countries"]) -> MetaOapg.properties.withheld_in_countries: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["event_at", "user", "withheld_in_countries", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        withheld_in_countries: typing.Union[MetaOapg.properties.withheld_in_countries, list, tuple, ],
        event_at: typing.Union[MetaOapg.properties.event_at, str, datetime, ],
        user: 'UserTakedownComplianceSchemaUser',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserTakedownComplianceSchema':
        return super().__new__(
            cls,
            *args,
            withheld_in_countries=withheld_in_countries,
            event_at=event_at,
            user=user,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.country_code import CountryCode
from x_python_sdk.model.user_takedown_compliance_schema_user import UserTakedownComplianceSchemaUser