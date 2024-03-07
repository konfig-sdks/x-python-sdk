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

from x_python_sdk.model.streaming_tweet_response import StreamingTweetResponse as StreamingTweetResponseSchema
from x_python_sdk.model.problem import Problem as ProblemSchema
from x_python_sdk.model.error import Error as ErrorSchema

from x_python_sdk.type.streaming_tweet_response import StreamingTweetResponse
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.error import Error

from ...api_client import Dictionary
from x_python_sdk.pydantic.error import Error as ErrorPydantic
from x_python_sdk.pydantic.streaming_tweet_response import StreamingTweetResponse as StreamingTweetResponsePydantic
from x_python_sdk.pydantic.problem import Problem as ProblemPydantic

# Query params


class BackfillMinutesSchema(
    schemas.Int32Schema
):
    pass


class TweetFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
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
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
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
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
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
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
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
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
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
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
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
        'backfill_minutes': typing.Union[BackfillMinutesSchema, decimal.Decimal, int, ],
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


request_query_backfill_minutes = api_client.QueryParameter(
    name="backfill_minutes",
    style=api_client.ParameterStyle.FORM,
    schema=BackfillMinutesSchema,
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
SchemaFor200ResponseBodyApplicationJson = StreamingTweetResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: StreamingTweetResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: StreamingTweetResponse


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
_all_accept_content_types = (
    'application/json',
    'application/problem+json',
)


class BaseApi(api_client.Api):

    def _stream_sample_mapped_args(
        self,
        backfill_minutes: typing.Optional[int] = None,
        tweet_fields: typing.Optional[typing.List[str]] = None,
        expansions: typing.Optional[typing.List[str]] = None,
        media_fields: typing.Optional[typing.List[str]] = None,
        poll_fields: typing.Optional[typing.List[str]] = None,
        user_fields: typing.Optional[typing.List[str]] = None,
        place_fields: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if backfill_minutes is not None:
            _query_params["backfill_minutes"] = backfill_minutes
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
        args.query = _query_params
        return args

    async def _astream_sample_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        Sample stream
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_backfill_minutes,
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
            path_template='/2/tweets/sample/stream',
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


    def _stream_sample_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        Sample stream
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_backfill_minutes,
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
            path_template='/2/tweets/sample/stream',
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


class StreamSampleRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def astream_sample(
        self,
        backfill_minutes: typing.Optional[int] = None,
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
        args = self._stream_sample_mapped_args(
            backfill_minutes=backfill_minutes,
            tweet_fields=tweet_fields,
            expansions=expansions,
            media_fields=media_fields,
            poll_fields=poll_fields,
            user_fields=user_fields,
            place_fields=place_fields,
        )
        return await self._astream_sample_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def stream_sample(
        self,
        backfill_minutes: typing.Optional[int] = None,
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
        args = self._stream_sample_mapped_args(
            backfill_minutes=backfill_minutes,
            tweet_fields=tweet_fields,
            expansions=expansions,
            media_fields=media_fields,
            poll_fields=poll_fields,
            user_fields=user_fields,
            place_fields=place_fields,
        )
        return self._stream_sample_oapg(
            query_params=args.query,
        )

class StreamSample(BaseApi):

    async def astream_sample(
        self,
        backfill_minutes: typing.Optional[int] = None,
        tweet_fields: typing.Optional[typing.List[str]] = None,
        expansions: typing.Optional[typing.List[str]] = None,
        media_fields: typing.Optional[typing.List[str]] = None,
        poll_fields: typing.Optional[typing.List[str]] = None,
        user_fields: typing.Optional[typing.List[str]] = None,
        place_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> StreamingTweetResponsePydantic:
        raw_response = await self.raw.astream_sample(
            backfill_minutes=backfill_minutes,
            tweet_fields=tweet_fields,
            expansions=expansions,
            media_fields=media_fields,
            poll_fields=poll_fields,
            user_fields=user_fields,
            place_fields=place_fields,
            **kwargs,
        )
        if validate:
            return StreamingTweetResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(StreamingTweetResponsePydantic, raw_response.body)
    
    
    def stream_sample(
        self,
        backfill_minutes: typing.Optional[int] = None,
        tweet_fields: typing.Optional[typing.List[str]] = None,
        expansions: typing.Optional[typing.List[str]] = None,
        media_fields: typing.Optional[typing.List[str]] = None,
        poll_fields: typing.Optional[typing.List[str]] = None,
        user_fields: typing.Optional[typing.List[str]] = None,
        place_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> StreamingTweetResponsePydantic:
        raw_response = self.raw.stream_sample(
            backfill_minutes=backfill_minutes,
            tweet_fields=tweet_fields,
            expansions=expansions,
            media_fields=media_fields,
            poll_fields=poll_fields,
            user_fields=user_fields,
            place_fields=place_fields,
        )
        if validate:
            return StreamingTweetResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(StreamingTweetResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        backfill_minutes: typing.Optional[int] = None,
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
        args = self._stream_sample_mapped_args(
            backfill_minutes=backfill_minutes,
            tweet_fields=tweet_fields,
            expansions=expansions,
            media_fields=media_fields,
            poll_fields=poll_fields,
            user_fields=user_fields,
            place_fields=place_fields,
        )
        return await self._astream_sample_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        backfill_minutes: typing.Optional[int] = None,
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
        args = self._stream_sample_mapped_args(
            backfill_minutes=backfill_minutes,
            tweet_fields=tweet_fields,
            expansions=expansions,
            media_fields=media_fields,
            poll_fields=poll_fields,
            user_fields=user_fields,
            place_fields=place_fields,
        )
        return self._stream_sample_oapg(
            query_params=args.query,
        )

