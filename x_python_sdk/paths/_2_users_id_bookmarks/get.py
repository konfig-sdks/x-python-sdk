# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.62
    Created by: https://developer.twitter.com/
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from x_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from x_python_sdk.api_response import AsyncGeneratorResponse
from x_python_sdk import api_client, exceptions
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

from x_python_sdk.model.problem import Problem as ProblemSchema
from x_python_sdk.model.get2_users_id_bookmarks_response import Get2UsersIdBookmarksResponse as Get2UsersIdBookmarksResponseSchema
from x_python_sdk.model.error import Error as ErrorSchema
from x_python_sdk.model.pagination_token36 import PaginationToken36 as PaginationToken36Schema

from x_python_sdk.type.get2_users_id_bookmarks_response import Get2UsersIdBookmarksResponse
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.pagination_token36 import PaginationToken36
from x_python_sdk.type.error import Error

from ...api_client import Dictionary
from x_python_sdk.pydantic.error import Error as ErrorPydantic
from x_python_sdk.pydantic.problem import Problem as ProblemPydantic
from x_python_sdk.pydantic.get2_users_id_bookmarks_response import Get2UsersIdBookmarksResponse as Get2UsersIdBookmarksResponsePydantic
from x_python_sdk.pydantic.pagination_token36 import PaginationToken36 as PaginationToken36Pydantic

from . import path

# Query params


class MaxResultsSchema(
    schemas.Int32Schema
):


    class MetaOapg:
        format = 'int32'
        inclusive_maximum = 100
        inclusive_minimum = 1
PaginationTokenSchema = schemas.Schema


class TweetFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        unique_items = True
        min_items = 1
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "attachments": "ATTACHMENTS",
                    "author_id": "AUTHOR_ID",
                    "context_annotations": "CONTEXT_ANNOTATIONS",
                    "conversation_id": "CONVERSATION_ID",
                    "created_at": "CREATED_AT",
                    "edit_controls": "EDIT_CONTROLS",
                    "edit_history_tweet_ids": "EDIT_HISTORY_TWEET_IDS",
                    "entities": "ENTITIES",
                    "geo": "GEO",
                    "id": "ID",
                    "in_reply_to_user_id": "IN_REPLY_TO_USER_ID",
                    "lang": "LANG",
                    "non_public_metrics": "NON_PUBLIC_METRICS",
                    "organic_metrics": "ORGANIC_METRICS",
                    "possibly_sensitive": "POSSIBLY_SENSITIVE",
                    "promoted_metrics": "PROMOTED_METRICS",
                    "public_metrics": "PUBLIC_METRICS",
                    "referenced_tweets": "REFERENCED_TWEETS",
                    "reply_settings": "REPLY_SETTINGS",
                    "source": "SOURCE",
                    "text": "TEXT",
                    "withheld": "WITHHELD",
                }
            
            @schemas.classproperty
            def ATTACHMENTS(cls):
                return cls("attachments")
            
            @schemas.classproperty
            def AUTHOR_ID(cls):
                return cls("author_id")
            
            @schemas.classproperty
            def CONTEXT_ANNOTATIONS(cls):
                return cls("context_annotations")
            
            @schemas.classproperty
            def CONVERSATION_ID(cls):
                return cls("conversation_id")
            
            @schemas.classproperty
            def CREATED_AT(cls):
                return cls("created_at")
            
            @schemas.classproperty
            def EDIT_CONTROLS(cls):
                return cls("edit_controls")
            
            @schemas.classproperty
            def EDIT_HISTORY_TWEET_IDS(cls):
                return cls("edit_history_tweet_ids")
            
            @schemas.classproperty
            def ENTITIES(cls):
                return cls("entities")
            
            @schemas.classproperty
            def GEO(cls):
                return cls("geo")
            
            @schemas.classproperty
            def ID(cls):
                return cls("id")
            
            @schemas.classproperty
            def IN_REPLY_TO_USER_ID(cls):
                return cls("in_reply_to_user_id")
            
            @schemas.classproperty
            def LANG(cls):
                return cls("lang")
            
            @schemas.classproperty
            def NON_PUBLIC_METRICS(cls):
                return cls("non_public_metrics")
            
            @schemas.classproperty
            def ORGANIC_METRICS(cls):
                return cls("organic_metrics")
            
            @schemas.classproperty
            def POSSIBLY_SENSITIVE(cls):
                return cls("possibly_sensitive")
            
            @schemas.classproperty
            def PROMOTED_METRICS(cls):
                return cls("promoted_metrics")
            
            @schemas.classproperty
            def PUBLIC_METRICS(cls):
                return cls("public_metrics")
            
            @schemas.classproperty
            def REFERENCED_TWEETS(cls):
                return cls("referenced_tweets")
            
            @schemas.classproperty
            def REPLY_SETTINGS(cls):
                return cls("reply_settings")
            
            @schemas.classproperty
            def SOURCE(cls):
                return cls("source")
            
            @schemas.classproperty
            def TEXT(cls):
                return cls("text")
            
            @schemas.classproperty
            def WITHHELD(cls):
                return cls("withheld")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TweetFieldsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class ExpansionsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        unique_items = True
        min_items = 1
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "attachments.media_keys": "ATTACHMENTS_MEDIA_KEYS",
                    "attachments.poll_ids": "ATTACHMENTS_POLL_IDS",
                    "author_id": "AUTHOR_ID",
                    "edit_history_tweet_ids": "EDIT_HISTORY_TWEET_IDS",
                    "entities.mentions.username": "ENTITIES_MENTIONS_USERNAME",
                    "geo.place_id": "GEO_PLACE_ID",
                    "in_reply_to_user_id": "IN_REPLY_TO_USER_ID",
                    "referenced_tweets.id": "REFERENCED_TWEETS_ID",
                    "referenced_tweets.id.author_id": "REFERENCED_TWEETS_ID_AUTHOR_ID",
                }
            
            @schemas.classproperty
            def ATTACHMENTS_MEDIA_KEYS(cls):
                return cls("attachments.media_keys")
            
            @schemas.classproperty
            def ATTACHMENTS_POLL_IDS(cls):
                return cls("attachments.poll_ids")
            
            @schemas.classproperty
            def AUTHOR_ID(cls):
                return cls("author_id")
            
            @schemas.classproperty
            def EDIT_HISTORY_TWEET_IDS(cls):
                return cls("edit_history_tweet_ids")
            
            @schemas.classproperty
            def ENTITIES_MENTIONS_USERNAME(cls):
                return cls("entities.mentions.username")
            
            @schemas.classproperty
            def GEO_PLACE_ID(cls):
                return cls("geo.place_id")
            
            @schemas.classproperty
            def IN_REPLY_TO_USER_ID(cls):
                return cls("in_reply_to_user_id")
            
            @schemas.classproperty
            def REFERENCED_TWEETS_ID(cls):
                return cls("referenced_tweets.id")
            
            @schemas.classproperty
            def REFERENCED_TWEETS_ID_AUTHOR_ID(cls):
                return cls("referenced_tweets.id.author_id")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ExpansionsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class MediaFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        unique_items = True
        min_items = 1
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "alt_text": "ALT_TEXT",
                    "duration_ms": "DURATION_MS",
                    "height": "HEIGHT",
                    "media_key": "MEDIA_KEY",
                    "non_public_metrics": "NON_PUBLIC_METRICS",
                    "organic_metrics": "ORGANIC_METRICS",
                    "preview_image_url": "PREVIEW_IMAGE_URL",
                    "promoted_metrics": "PROMOTED_METRICS",
                    "public_metrics": "PUBLIC_METRICS",
                    "type": "TYPE",
                    "url": "URL",
                    "variants": "VARIANTS",
                    "width": "WIDTH",
                }
            
            @schemas.classproperty
            def ALT_TEXT(cls):
                return cls("alt_text")
            
            @schemas.classproperty
            def DURATION_MS(cls):
                return cls("duration_ms")
            
            @schemas.classproperty
            def HEIGHT(cls):
                return cls("height")
            
            @schemas.classproperty
            def MEDIA_KEY(cls):
                return cls("media_key")
            
            @schemas.classproperty
            def NON_PUBLIC_METRICS(cls):
                return cls("non_public_metrics")
            
            @schemas.classproperty
            def ORGANIC_METRICS(cls):
                return cls("organic_metrics")
            
            @schemas.classproperty
            def PREVIEW_IMAGE_URL(cls):
                return cls("preview_image_url")
            
            @schemas.classproperty
            def PROMOTED_METRICS(cls):
                return cls("promoted_metrics")
            
            @schemas.classproperty
            def PUBLIC_METRICS(cls):
                return cls("public_metrics")
            
            @schemas.classproperty
            def TYPE(cls):
                return cls("type")
            
            @schemas.classproperty
            def URL(cls):
                return cls("url")
            
            @schemas.classproperty
            def VARIANTS(cls):
                return cls("variants")
            
            @schemas.classproperty
            def WIDTH(cls):
                return cls("width")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MediaFieldsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class PollFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        unique_items = True
        min_items = 1
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "duration_minutes": "DURATION_MINUTES",
                    "end_datetime": "END_DATETIME",
                    "id": "ID",
                    "options": "OPTIONS",
                    "voting_status": "VOTING_STATUS",
                }
            
            @schemas.classproperty
            def DURATION_MINUTES(cls):
                return cls("duration_minutes")
            
            @schemas.classproperty
            def END_DATETIME(cls):
                return cls("end_datetime")
            
            @schemas.classproperty
            def ID(cls):
                return cls("id")
            
            @schemas.classproperty
            def OPTIONS(cls):
                return cls("options")
            
            @schemas.classproperty
            def VOTING_STATUS(cls):
                return cls("voting_status")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PollFieldsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class UserFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        unique_items = True
        min_items = 1
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "created_at": "CREATED_AT",
                    "description": "DESCRIPTION",
                    "entities": "ENTITIES",
                    "id": "ID",
                    "location": "LOCATION",
                    "name": "NAME",
                    "pinned_tweet_id": "PINNED_TWEET_ID",
                    "profile_image_url": "PROFILE_IMAGE_URL",
                    "protected": "PROTECTED",
                    "public_metrics": "PUBLIC_METRICS",
                    "url": "URL",
                    "username": "USERNAME",
                    "verified": "VERIFIED",
                    "verified_type": "VERIFIED_TYPE",
                    "withheld": "WITHHELD",
                }
            
            @schemas.classproperty
            def CREATED_AT(cls):
                return cls("created_at")
            
            @schemas.classproperty
            def DESCRIPTION(cls):
                return cls("description")
            
            @schemas.classproperty
            def ENTITIES(cls):
                return cls("entities")
            
            @schemas.classproperty
            def ID(cls):
                return cls("id")
            
            @schemas.classproperty
            def LOCATION(cls):
                return cls("location")
            
            @schemas.classproperty
            def NAME(cls):
                return cls("name")
            
            @schemas.classproperty
            def PINNED_TWEET_ID(cls):
                return cls("pinned_tweet_id")
            
            @schemas.classproperty
            def PROFILE_IMAGE_URL(cls):
                return cls("profile_image_url")
            
            @schemas.classproperty
            def PROTECTED(cls):
                return cls("protected")
            
            @schemas.classproperty
            def PUBLIC_METRICS(cls):
                return cls("public_metrics")
            
            @schemas.classproperty
            def URL(cls):
                return cls("url")
            
            @schemas.classproperty
            def USERNAME(cls):
                return cls("username")
            
            @schemas.classproperty
            def VERIFIED(cls):
                return cls("verified")
            
            @schemas.classproperty
            def VERIFIED_TYPE(cls):
                return cls("verified_type")
            
            @schemas.classproperty
            def WITHHELD(cls):
                return cls("withheld")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'UserFieldsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class PlaceFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        unique_items = True
        min_items = 1
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "contained_within": "CONTAINED_WITHIN",
                    "country": "COUNTRY",
                    "country_code": "COUNTRY_CODE",
                    "full_name": "FULL_NAME",
                    "geo": "GEO",
                    "id": "ID",
                    "name": "NAME",
                    "place_type": "PLACE_TYPE",
                }
            
            @schemas.classproperty
            def CONTAINED_WITHIN(cls):
                return cls("contained_within")
            
            @schemas.classproperty
            def COUNTRY(cls):
                return cls("country")
            
            @schemas.classproperty
            def COUNTRY_CODE(cls):
                return cls("country_code")
            
            @schemas.classproperty
            def FULL_NAME(cls):
                return cls("full_name")
            
            @schemas.classproperty
            def GEO(cls):
                return cls("geo")
            
            @schemas.classproperty
            def ID(cls):
                return cls("id")
            
            @schemas.classproperty
            def NAME(cls):
                return cls("name")
            
            @schemas.classproperty
            def PLACE_TYPE(cls):
                return cls("place_type")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PlaceFieldsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'max_results': typing.Union[MaxResultsSchema, decimal.Decimal, int, ],
        'pagination_token': typing.Union[PaginationTokenSchema, ],
        'tweet.fields': typing.Union[TweetFieldsSchema, list, tuple, ],
        'expansions': typing.Union[ExpansionsSchema, list, tuple, ],
        'media.fields': typing.Union[MediaFieldsSchema, list, tuple, ],
        'poll.fields': typing.Union[PollFieldsSchema, list, tuple, ],
        'user.fields': typing.Union[UserFieldsSchema, list, tuple, ],
        'place.fields': typing.Union[PlaceFieldsSchema, list, tuple, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_max_results = api_client.QueryParameter(
    name="max_results",
    style=api_client.ParameterStyle.FORM,
    schema=MaxResultsSchema,
    explode=True,
)
request_query_pagination_token = api_client.QueryParameter(
    name="pagination_token",
    style=api_client.ParameterStyle.FORM,
    schema=PaginationToken36Schema,
    explode=True,
)
request_query_tweet_fields = api_client.QueryParameter(
    name="tweet.fields",
    style=api_client.ParameterStyle.FORM,
    schema=TweetFieldsSchema,
)
request_query_expansions = api_client.QueryParameter(
    name="expansions",
    style=api_client.ParameterStyle.FORM,
    schema=ExpansionsSchema,
)
request_query_media_fields = api_client.QueryParameter(
    name="media.fields",
    style=api_client.ParameterStyle.FORM,
    schema=MediaFieldsSchema,
)
request_query_poll_fields = api_client.QueryParameter(
    name="poll.fields",
    style=api_client.ParameterStyle.FORM,
    schema=PollFieldsSchema,
)
request_query_user_fields = api_client.QueryParameter(
    name="user.fields",
    style=api_client.ParameterStyle.FORM,
    schema=UserFieldsSchema,
)
request_query_place_fields = api_client.QueryParameter(
    name="place.fields",
    style=api_client.ParameterStyle.FORM,
    schema=PlaceFieldsSchema,
)
# Path params
IdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'id': typing.Union[IdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_id = api_client.PathParameter(
    name="id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
_auth = [
    'OAuth2UserToken',
]
SchemaFor200ResponseBodyApplicationJson = Get2UsersIdBookmarksResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Get2UsersIdBookmarksResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Get2UsersIdBookmarksResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = ErrorSchema
SchemaFor0ResponseBodyApplicationProblemjson = ProblemSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: Error


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationProblemjson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
    'application/problem+json',
)


class BaseApi(api_client.Api):

    def _get_user_bookmarks_mapped_args(
        self,
        id: str,
        max_results: typing.Optional[int] = None,
        pagination_token: typing.Optional[PaginationToken36] = None,
        tweet_fields: typing.Optional[typing.List[str]] = None,
        expansions: typing.Optional[typing.List[str]] = None,
        media_fields: typing.Optional[typing.List[str]] = None,
        poll_fields: typing.Optional[typing.List[str]] = None,
        user_fields: typing.Optional[typing.List[str]] = None,
        place_fields: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if max_results is not None:
            _query_params["max_results"] = max_results
        if pagination_token is not None:
            _query_params["pagination_token"] = pagination_token
        if tweet_fields is not None:
            _query_params["tweet.fields"] = tweet_fields
        if expansions is not None:
            _query_params["expansions"] = expansions
        if media_fields is not None:
            _query_params["media.fields"] = media_fields
        if poll_fields is not None:
            _query_params["poll.fields"] = poll_fields
        if user_fields is not None:
            _query_params["user.fields"] = user_fields
        if place_fields is not None:
            _query_params["place.fields"] = place_fields
        if id is not None:
            _path_params["id"] = id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_user_bookmarks_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Bookmarks by User
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_max_results,
            request_query_pagination_token,
            request_query_tweet_fields,
            request_query_expansions,
            request_query_media_fields,
            request_query_poll_fields,
            request_query_user_fields,
            request_query_place_fields,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/2/users/{id}/bookmarks',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_user_bookmarks_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Bookmarks by User
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_max_results,
            request_query_pagination_token,
            request_query_tweet_fields,
            request_query_expansions,
            request_query_media_fields,
            request_query_poll_fields,
            request_query_user_fields,
            request_query_place_fields,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/2/users/{id}/bookmarks',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetUserBookmarksRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_user_bookmarks(
        self,
        id: str,
        max_results: typing.Optional[int] = None,
        pagination_token: typing.Optional[PaginationToken36] = None,
        tweet_fields: typing.Optional[typing.List[str]] = None,
        expansions: typing.Optional[typing.List[str]] = None,
        media_fields: typing.Optional[typing.List[str]] = None,
        poll_fields: typing.Optional[typing.List[str]] = None,
        user_fields: typing.Optional[typing.List[str]] = None,
        place_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_bookmarks_mapped_args(
            id=id,
            max_results=max_results,
            pagination_token=pagination_token,
            tweet_fields=tweet_fields,
            expansions=expansions,
            media_fields=media_fields,
            poll_fields=poll_fields,
            user_fields=user_fields,
            place_fields=place_fields,
        )
        return await self._aget_user_bookmarks_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_user_bookmarks(
        self,
        id: str,
        max_results: typing.Optional[int] = None,
        pagination_token: typing.Optional[PaginationToken36] = None,
        tweet_fields: typing.Optional[typing.List[str]] = None,
        expansions: typing.Optional[typing.List[str]] = None,
        media_fields: typing.Optional[typing.List[str]] = None,
        poll_fields: typing.Optional[typing.List[str]] = None,
        user_fields: typing.Optional[typing.List[str]] = None,
        place_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_bookmarks_mapped_args(
            id=id,
            max_results=max_results,
            pagination_token=pagination_token,
            tweet_fields=tweet_fields,
            expansions=expansions,
            media_fields=media_fields,
            poll_fields=poll_fields,
            user_fields=user_fields,
            place_fields=place_fields,
        )
        return self._get_user_bookmarks_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetUserBookmarks(BaseApi):

    async def aget_user_bookmarks(
        self,
        id: str,
        max_results: typing.Optional[int] = None,
        pagination_token: typing.Optional[PaginationToken36] = None,
        tweet_fields: typing.Optional[typing.List[str]] = None,
        expansions: typing.Optional[typing.List[str]] = None,
        media_fields: typing.Optional[typing.List[str]] = None,
        poll_fields: typing.Optional[typing.List[str]] = None,
        user_fields: typing.Optional[typing.List[str]] = None,
        place_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> Get2UsersIdBookmarksResponsePydantic:
        raw_response = await self.raw.aget_user_bookmarks(
            id=id,
            max_results=max_results,
            pagination_token=pagination_token,
            tweet_fields=tweet_fields,
            expansions=expansions,
            media_fields=media_fields,
            poll_fields=poll_fields,
            user_fields=user_fields,
            place_fields=place_fields,
            **kwargs,
        )
        if validate:
            return Get2UsersIdBookmarksResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(Get2UsersIdBookmarksResponsePydantic, raw_response.body)
    
    
    def get_user_bookmarks(
        self,
        id: str,
        max_results: typing.Optional[int] = None,
        pagination_token: typing.Optional[PaginationToken36] = None,
        tweet_fields: typing.Optional[typing.List[str]] = None,
        expansions: typing.Optional[typing.List[str]] = None,
        media_fields: typing.Optional[typing.List[str]] = None,
        poll_fields: typing.Optional[typing.List[str]] = None,
        user_fields: typing.Optional[typing.List[str]] = None,
        place_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> Get2UsersIdBookmarksResponsePydantic:
        raw_response = self.raw.get_user_bookmarks(
            id=id,
            max_results=max_results,
            pagination_token=pagination_token,
            tweet_fields=tweet_fields,
            expansions=expansions,
            media_fields=media_fields,
            poll_fields=poll_fields,
            user_fields=user_fields,
            place_fields=place_fields,
        )
        if validate:
            return Get2UsersIdBookmarksResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(Get2UsersIdBookmarksResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        id: str,
        max_results: typing.Optional[int] = None,
        pagination_token: typing.Optional[PaginationToken36] = None,
        tweet_fields: typing.Optional[typing.List[str]] = None,
        expansions: typing.Optional[typing.List[str]] = None,
        media_fields: typing.Optional[typing.List[str]] = None,
        poll_fields: typing.Optional[typing.List[str]] = None,
        user_fields: typing.Optional[typing.List[str]] = None,
        place_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_bookmarks_mapped_args(
            id=id,
            max_results=max_results,
            pagination_token=pagination_token,
            tweet_fields=tweet_fields,
            expansions=expansions,
            media_fields=media_fields,
            poll_fields=poll_fields,
            user_fields=user_fields,
            place_fields=place_fields,
        )
        return await self._aget_user_bookmarks_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        id: str,
        max_results: typing.Optional[int] = None,
        pagination_token: typing.Optional[PaginationToken36] = None,
        tweet_fields: typing.Optional[typing.List[str]] = None,
        expansions: typing.Optional[typing.List[str]] = None,
        media_fields: typing.Optional[typing.List[str]] = None,
        poll_fields: typing.Optional[typing.List[str]] = None,
        user_fields: typing.Optional[typing.List[str]] = None,
        place_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_bookmarks_mapped_args(
            id=id,
            max_results=max_results,
            pagination_token=pagination_token,
            tweet_fields=tweet_fields,
            expansions=expansions,
            media_fields=media_fields,
            poll_fields=poll_fields,
            user_fields=user_fields,
            place_fields=place_fields,
        )
        return self._get_user_bookmarks_oapg(
            query_params=args.query,
            path_params=args.path,
        )

