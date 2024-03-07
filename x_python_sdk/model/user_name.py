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


class UserName(
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The Twitter handle (screen name) of this user.
    """


    class MetaOapg:
        regex=[{
            'pattern': r'^[A-Za-z0-9_]{1,15}$',
        }]
