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


class PlaceType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "poi": "POI",
            "neighborhood": "NEIGHBORHOOD",
            "city": "CITY",
            "admin": "ADMIN",
            "country": "COUNTRY",
            "unknown": "UNKNOWN",
        }
    
    @schemas.classproperty
    def POI(cls):
        return cls("poi")
    
    @schemas.classproperty
    def NEIGHBORHOOD(cls):
        return cls("neighborhood")
    
    @schemas.classproperty
    def CITY(cls):
        return cls("city")
    
    @schemas.classproperty
    def ADMIN(cls):
        return cls("admin")
    
    @schemas.classproperty
    def COUNTRY(cls):
        return cls("country")
    
    @schemas.classproperty
    def UNKNOWN(cls):
        return cls("unknown")
