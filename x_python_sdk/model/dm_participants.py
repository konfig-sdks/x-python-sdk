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


class DmParticipants(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Participants for the DM Conversation.
    """


    class MetaOapg:
        max_items = 49
        min_items = 2
        
        @staticmethod
        def items() -> typing.Type['UserId']:
            return UserId

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['UserId'], typing.List['UserId']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DmParticipants':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'UserId':
        return super().__getitem__(i)

from x_python_sdk.model.user_id import UserId