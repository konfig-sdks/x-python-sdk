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


class TweetEditControls(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "is_edit_eligible",
            "edits_remaining",
            "editable_until",
        }
        
        class properties:
            editable_until = schemas.DateTimeSchema
            edits_remaining = schemas.IntSchema
            is_edit_eligible = schemas.BoolSchema
            __annotations__ = {
                "editable_until": editable_until,
                "edits_remaining": edits_remaining,
                "is_edit_eligible": is_edit_eligible,
            }
    
    is_edit_eligible: MetaOapg.properties.is_edit_eligible
    edits_remaining: MetaOapg.properties.edits_remaining
    editable_until: MetaOapg.properties.editable_until
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["editable_until"]) -> MetaOapg.properties.editable_until: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edits_remaining"]) -> MetaOapg.properties.edits_remaining: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_edit_eligible"]) -> MetaOapg.properties.is_edit_eligible: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["editable_until", "edits_remaining", "is_edit_eligible", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["editable_until"]) -> MetaOapg.properties.editable_until: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edits_remaining"]) -> MetaOapg.properties.edits_remaining: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_edit_eligible"]) -> MetaOapg.properties.is_edit_eligible: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["editable_until", "edits_remaining", "is_edit_eligible", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        is_edit_eligible: typing.Union[MetaOapg.properties.is_edit_eligible, bool, ],
        edits_remaining: typing.Union[MetaOapg.properties.edits_remaining, decimal.Decimal, int, ],
        editable_until: typing.Union[MetaOapg.properties.editable_until, str, datetime, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TweetEditControls':
        return super().__new__(
            cls,
            *args,
            is_edit_eligible=is_edit_eligible,
            edits_remaining=edits_remaining,
            editable_until=editable_until,
            _configuration=_configuration,
            **kwargs,
        )