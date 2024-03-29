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


class Photo(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def discriminator():
            return {
                'type': {
                    'animated_gif': AnimatedGif,
                    'photo': Photo,
                    'video': Video,
                }
            }
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    alt_text = schemas.StrSchema
                    url = schemas.StrSchema
                    __annotations__ = {
                        "alt_text": alt_text,
                        "url": url,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["alt_text"]) -> MetaOapg.properties.alt_text: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["alt_text", "url", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["alt_text"]) -> typing.Union[MetaOapg.properties.alt_text, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["alt_text", "url", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                alt_text: typing.Union[MetaOapg.properties.alt_text, str, schemas.Unset] = schemas.unset,
                url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    alt_text=alt_text,
                    url=url,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                Media,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Photo':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.animated_gif import AnimatedGif
from x_python_sdk.model.media import Media
from x_python_sdk.model.photo import Photo
from x_python_sdk.model.video import Video
