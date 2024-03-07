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


class Geo(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "bbox",
            "type",
            "properties",
        }
        
        class properties:
        
            @staticmethod
            def bbox() -> typing.Type['GeoBbox']:
                return GeoBbox
            properties = schemas.DictSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FEATURE(cls):
                    return cls("Feature")
        
            @staticmethod
            def geometry() -> typing.Type['Point']:
                return Point
            __annotations__ = {
                "bbox": bbox,
                "properties": properties,
                "type": type,
                "geometry": geometry,
            }
    
    bbox: 'GeoBbox'
    type: MetaOapg.properties.type
    properties: MetaOapg.properties.properties
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bbox"]) -> 'GeoBbox': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["properties"]) -> MetaOapg.properties.properties: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["geometry"]) -> 'Point': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bbox", "properties", "type", "geometry", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bbox"]) -> 'GeoBbox': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["properties"]) -> MetaOapg.properties.properties: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["geometry"]) -> typing.Union['Point', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bbox", "properties", "type", "geometry", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bbox: 'GeoBbox',
        type: typing.Union[MetaOapg.properties.type, str, ],
        properties: typing.Union[MetaOapg.properties.properties, dict, frozendict.frozendict, ],
        geometry: typing.Union['Point', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Geo':
        return super().__new__(
            cls,
            *args,
            bbox=bbox,
            type=type,
            properties=properties,
            geometry=geometry,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.geo_bbox import GeoBbox
from x_python_sdk.model.point import Point