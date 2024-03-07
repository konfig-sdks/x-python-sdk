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


class Video(
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
                    duration_ms = schemas.IntSchema
                    
                    
                    class non_public_metrics(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                playback_0_count = schemas.Int32Schema
                                playback_100_count = schemas.Int32Schema
                                playback_25_count = schemas.Int32Schema
                                playback_50_count = schemas.Int32Schema
                                playback_75_count = schemas.Int32Schema
                                __annotations__ = {
                                    "playback_0_count": playback_0_count,
                                    "playback_100_count": playback_100_count,
                                    "playback_25_count": playback_25_count,
                                    "playback_50_count": playback_50_count,
                                    "playback_75_count": playback_75_count,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["playback_0_count"]) -> MetaOapg.properties.playback_0_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["playback_100_count"]) -> MetaOapg.properties.playback_100_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["playback_25_count"]) -> MetaOapg.properties.playback_25_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["playback_50_count"]) -> MetaOapg.properties.playback_50_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["playback_75_count"]) -> MetaOapg.properties.playback_75_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["playback_0_count", "playback_100_count", "playback_25_count", "playback_50_count", "playback_75_count", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["playback_0_count"]) -> typing.Union[MetaOapg.properties.playback_0_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["playback_100_count"]) -> typing.Union[MetaOapg.properties.playback_100_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["playback_25_count"]) -> typing.Union[MetaOapg.properties.playback_25_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["playback_50_count"]) -> typing.Union[MetaOapg.properties.playback_50_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["playback_75_count"]) -> typing.Union[MetaOapg.properties.playback_75_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["playback_0_count", "playback_100_count", "playback_25_count", "playback_50_count", "playback_75_count", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            playback_0_count: typing.Union[MetaOapg.properties.playback_0_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            playback_100_count: typing.Union[MetaOapg.properties.playback_100_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            playback_25_count: typing.Union[MetaOapg.properties.playback_25_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            playback_50_count: typing.Union[MetaOapg.properties.playback_50_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            playback_75_count: typing.Union[MetaOapg.properties.playback_75_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'non_public_metrics':
                            return super().__new__(
                                cls,
                                *args,
                                playback_0_count=playback_0_count,
                                playback_100_count=playback_100_count,
                                playback_25_count=playback_25_count,
                                playback_50_count=playback_50_count,
                                playback_75_count=playback_75_count,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class organic_metrics(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                playback_0_count = schemas.Int32Schema
                                playback_100_count = schemas.Int32Schema
                                playback_25_count = schemas.Int32Schema
                                playback_50_count = schemas.Int32Schema
                                playback_75_count = schemas.Int32Schema
                                view_count = schemas.Int32Schema
                                __annotations__ = {
                                    "playback_0_count": playback_0_count,
                                    "playback_100_count": playback_100_count,
                                    "playback_25_count": playback_25_count,
                                    "playback_50_count": playback_50_count,
                                    "playback_75_count": playback_75_count,
                                    "view_count": view_count,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["playback_0_count"]) -> MetaOapg.properties.playback_0_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["playback_100_count"]) -> MetaOapg.properties.playback_100_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["playback_25_count"]) -> MetaOapg.properties.playback_25_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["playback_50_count"]) -> MetaOapg.properties.playback_50_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["playback_75_count"]) -> MetaOapg.properties.playback_75_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["view_count"]) -> MetaOapg.properties.view_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["playback_0_count", "playback_100_count", "playback_25_count", "playback_50_count", "playback_75_count", "view_count", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["playback_0_count"]) -> typing.Union[MetaOapg.properties.playback_0_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["playback_100_count"]) -> typing.Union[MetaOapg.properties.playback_100_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["playback_25_count"]) -> typing.Union[MetaOapg.properties.playback_25_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["playback_50_count"]) -> typing.Union[MetaOapg.properties.playback_50_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["playback_75_count"]) -> typing.Union[MetaOapg.properties.playback_75_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["view_count"]) -> typing.Union[MetaOapg.properties.view_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["playback_0_count", "playback_100_count", "playback_25_count", "playback_50_count", "playback_75_count", "view_count", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            playback_0_count: typing.Union[MetaOapg.properties.playback_0_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            playback_100_count: typing.Union[MetaOapg.properties.playback_100_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            playback_25_count: typing.Union[MetaOapg.properties.playback_25_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            playback_50_count: typing.Union[MetaOapg.properties.playback_50_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            playback_75_count: typing.Union[MetaOapg.properties.playback_75_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            view_count: typing.Union[MetaOapg.properties.view_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'organic_metrics':
                            return super().__new__(
                                cls,
                                *args,
                                playback_0_count=playback_0_count,
                                playback_100_count=playback_100_count,
                                playback_25_count=playback_25_count,
                                playback_50_count=playback_50_count,
                                playback_75_count=playback_75_count,
                                view_count=view_count,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    preview_image_url = schemas.StrSchema
                    
                    
                    class promoted_metrics(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                playback_0_count = schemas.Int32Schema
                                playback_100_count = schemas.Int32Schema
                                playback_25_count = schemas.Int32Schema
                                playback_50_count = schemas.Int32Schema
                                playback_75_count = schemas.Int32Schema
                                view_count = schemas.Int32Schema
                                __annotations__ = {
                                    "playback_0_count": playback_0_count,
                                    "playback_100_count": playback_100_count,
                                    "playback_25_count": playback_25_count,
                                    "playback_50_count": playback_50_count,
                                    "playback_75_count": playback_75_count,
                                    "view_count": view_count,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["playback_0_count"]) -> MetaOapg.properties.playback_0_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["playback_100_count"]) -> MetaOapg.properties.playback_100_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["playback_25_count"]) -> MetaOapg.properties.playback_25_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["playback_50_count"]) -> MetaOapg.properties.playback_50_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["playback_75_count"]) -> MetaOapg.properties.playback_75_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["view_count"]) -> MetaOapg.properties.view_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["playback_0_count", "playback_100_count", "playback_25_count", "playback_50_count", "playback_75_count", "view_count", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["playback_0_count"]) -> typing.Union[MetaOapg.properties.playback_0_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["playback_100_count"]) -> typing.Union[MetaOapg.properties.playback_100_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["playback_25_count"]) -> typing.Union[MetaOapg.properties.playback_25_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["playback_50_count"]) -> typing.Union[MetaOapg.properties.playback_50_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["playback_75_count"]) -> typing.Union[MetaOapg.properties.playback_75_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["view_count"]) -> typing.Union[MetaOapg.properties.view_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["playback_0_count", "playback_100_count", "playback_25_count", "playback_50_count", "playback_75_count", "view_count", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            playback_0_count: typing.Union[MetaOapg.properties.playback_0_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            playback_100_count: typing.Union[MetaOapg.properties.playback_100_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            playback_25_count: typing.Union[MetaOapg.properties.playback_25_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            playback_50_count: typing.Union[MetaOapg.properties.playback_50_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            playback_75_count: typing.Union[MetaOapg.properties.playback_75_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            view_count: typing.Union[MetaOapg.properties.view_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'promoted_metrics':
                            return super().__new__(
                                cls,
                                *args,
                                playback_0_count=playback_0_count,
                                playback_100_count=playback_100_count,
                                playback_25_count=playback_25_count,
                                playback_50_count=playback_50_count,
                                playback_75_count=playback_75_count,
                                view_count=view_count,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class public_metrics(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                view_count = schemas.Int32Schema
                                __annotations__ = {
                                    "view_count": view_count,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["view_count"]) -> MetaOapg.properties.view_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["view_count", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["view_count"]) -> typing.Union[MetaOapg.properties.view_count, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["view_count", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            view_count: typing.Union[MetaOapg.properties.view_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'public_metrics':
                            return super().__new__(
                                cls,
                                *args,
                                view_count=view_count,
                                _configuration=_configuration,
                                **kwargs,
                            )
                
                    @staticmethod
                    def variants() -> typing.Type['Variants']:
                        return Variants
                    __annotations__ = {
                        "duration_ms": duration_ms,
                        "non_public_metrics": non_public_metrics,
                        "organic_metrics": organic_metrics,
                        "preview_image_url": preview_image_url,
                        "promoted_metrics": promoted_metrics,
                        "public_metrics": public_metrics,
                        "variants": variants,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["duration_ms"]) -> MetaOapg.properties.duration_ms: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["non_public_metrics"]) -> MetaOapg.properties.non_public_metrics: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["organic_metrics"]) -> MetaOapg.properties.organic_metrics: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["preview_image_url"]) -> MetaOapg.properties.preview_image_url: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["promoted_metrics"]) -> MetaOapg.properties.promoted_metrics: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["public_metrics"]) -> MetaOapg.properties.public_metrics: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["variants"]) -> 'Variants': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["duration_ms", "non_public_metrics", "organic_metrics", "preview_image_url", "promoted_metrics", "public_metrics", "variants", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["duration_ms"]) -> typing.Union[MetaOapg.properties.duration_ms, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["non_public_metrics"]) -> typing.Union[MetaOapg.properties.non_public_metrics, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["organic_metrics"]) -> typing.Union[MetaOapg.properties.organic_metrics, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["preview_image_url"]) -> typing.Union[MetaOapg.properties.preview_image_url, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["promoted_metrics"]) -> typing.Union[MetaOapg.properties.promoted_metrics, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["public_metrics"]) -> typing.Union[MetaOapg.properties.public_metrics, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["variants"]) -> typing.Union['Variants', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["duration_ms", "non_public_metrics", "organic_metrics", "preview_image_url", "promoted_metrics", "public_metrics", "variants", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                duration_ms: typing.Union[MetaOapg.properties.duration_ms, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                non_public_metrics: typing.Union[MetaOapg.properties.non_public_metrics, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                organic_metrics: typing.Union[MetaOapg.properties.organic_metrics, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                preview_image_url: typing.Union[MetaOapg.properties.preview_image_url, str, schemas.Unset] = schemas.unset,
                promoted_metrics: typing.Union[MetaOapg.properties.promoted_metrics, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                public_metrics: typing.Union[MetaOapg.properties.public_metrics, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                variants: typing.Union['Variants', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    duration_ms=duration_ms,
                    non_public_metrics=non_public_metrics,
                    organic_metrics=organic_metrics,
                    preview_image_url=preview_image_url,
                    promoted_metrics=promoted_metrics,
                    public_metrics=public_metrics,
                    variants=variants,
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
    ) -> 'Video':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.animated_gif import AnimatedGif
from x_python_sdk.model.media import Media
from x_python_sdk.model.photo import Photo
from x_python_sdk.model.variants import Variants
from x_python_sdk.model.video import Video