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

from x_python_sdk.model.tweet_id import TweetId as TweetIdSchema
from x_python_sdk.model.problem import Problem as ProblemSchema
from x_python_sdk.model.get2_tweets_counts_all_response import Get2TweetsCountsAllResponse as Get2TweetsCountsAllResponseSchema
from x_python_sdk.model.error import Error as ErrorSchema
from x_python_sdk.model.pagination_token36 import PaginationToken36 as PaginationToken36Schema

from x_python_sdk.type.get2_tweets_counts_all_response import Get2TweetsCountsAllResponse
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.pagination_token36 import PaginationToken36
from x_python_sdk.type.error import Error
from x_python_sdk.type.tweet_id import TweetId

from ...api_client import Dictionary
from x_python_sdk.pydantic.error import Error as ErrorPydantic
from x_python_sdk.pydantic.get2_tweets_counts_all_response import Get2TweetsCountsAllResponse as Get2TweetsCountsAllResponsePydantic
from x_python_sdk.pydantic.problem import Problem as ProblemPydantic
from x_python_sdk.pydantic.tweet_id import TweetId as TweetIdPydantic
from x_python_sdk.pydantic.pagination_token36 import PaginationToken36 as PaginationToken36Pydantic

from . import path

# Query params


class QuerySchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 4096
        min_length = 1
StartTimeSchema = schemas.DateTimeSchema
EndTimeSchema = schemas.DateTimeSchema
SinceIdSchema = schemas.Schema
UntilIdSchema = schemas.Schema
NextTokenSchema = schemas.Schema
PaginationTokenSchema = schemas.Schema


class GranularitySchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "minute": "MINUTE",
            "hour": "HOUR",
            "day": "DAY",
        }
    
    @schemas.classproperty
    def MINUTE(cls):
        return cls("minute")
    
    @schemas.classproperty
    def HOUR(cls):
        return cls("hour")
    
    @schemas.classproperty
    def DAY(cls):
        return cls("day")


class SearchCountFieldsSchema(
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
                    "end": "END",
                    "start": "START",
                    "tweet_count": "TWEET_COUNT",
                }
            
            @schemas.classproperty
            def END(cls):
                return cls("end")
            
            @schemas.classproperty
            def START(cls):
                return cls("start")
            
            @schemas.classproperty
            def TWEET_COUNT(cls):
                return cls("tweet_count")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SearchCountFieldsSchema':
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
        'query': typing.Union[QuerySchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'start_time': typing.Union[StartTimeSchema, str, datetime, ],
        'end_time': typing.Union[EndTimeSchema, str, datetime, ],
        'since_id': typing.Union[SinceIdSchema, ],
        'until_id': typing.Union[UntilIdSchema, ],
        'next_token': typing.Union[NextTokenSchema, ],
        'pagination_token': typing.Union[PaginationTokenSchema, ],
        'granularity': typing.Union[GranularitySchema, str, ],
        'search_count.fields': typing.Union[SearchCountFieldsSchema, list, tuple, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_query = api_client.QueryParameter(
    name="query",
    style=api_client.ParameterStyle.FORM,
    schema=QuerySchema,
    required=True,
    explode=True,
)
request_query_start_time = api_client.QueryParameter(
    name="start_time",
    style=api_client.ParameterStyle.FORM,
    schema=StartTimeSchema,
    explode=True,
)
request_query_end_time = api_client.QueryParameter(
    name="end_time",
    style=api_client.ParameterStyle.FORM,
    schema=EndTimeSchema,
    explode=True,
)
request_query_since_id = api_client.QueryParameter(
    name="since_id",
    style=api_client.ParameterStyle.FORM,
    schema=TweetId,
    explode=True,
)
request_query_until_id = api_client.QueryParameter(
    name="until_id",
    style=api_client.ParameterStyle.FORM,
    schema=TweetId,
    explode=True,
)
request_query_next_token = api_client.QueryParameter(
    name="next_token",
    style=api_client.ParameterStyle.FORM,
    schema=PaginationToken36,
    explode=True,
)
request_query_pagination_token = api_client.QueryParameter(
    name="pagination_token",
    style=api_client.ParameterStyle.FORM,
    schema=PaginationToken36,
    explode=True,
)
request_query_granularity = api_client.QueryParameter(
    name="granularity",
    style=api_client.ParameterStyle.FORM,
    schema=GranularitySchema,
    explode=True,
)
request_query_search_count_fields = api_client.QueryParameter(
    name="search_count.fields",
    style=api_client.ParameterStyle.FORM,
    schema=SearchCountFieldsSchema,
)
_auth = [
    'BearerToken',
]
SchemaFor200ResponseBodyApplicationJson = Get2TweetsCountsAllResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Get2TweetsCountsAllResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Get2TweetsCountsAllResponse


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

    def _get_tweet_counts_mapped_args(
        self,
        query: str,
        start_time: typing.Optional[datetime] = None,
        end_time: typing.Optional[datetime] = None,
        since_id: typing.Optional[TweetId] = None,
        until_id: typing.Optional[TweetId] = None,
        next_token: typing.Optional[PaginationToken36] = None,
        pagination_token: typing.Optional[PaginationToken36] = None,
        granularity: typing.Optional[str] = None,
        search_count_fields: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if query is not None:
            _query_params["query"] = query
        if start_time is not None:
            _query_params["start_time"] = start_time
        if end_time is not None:
            _query_params["end_time"] = end_time
        if since_id is not None:
            _query_params["since_id"] = since_id
        if until_id is not None:
            _query_params["until_id"] = until_id
        if next_token is not None:
            _query_params["next_token"] = next_token
        if pagination_token is not None:
            _query_params["pagination_token"] = pagination_token
        if granularity is not None:
            _query_params["granularity"] = granularity
        if search_count_fields is not None:
            _query_params["search_count.fields"] = search_count_fields
        args.query = _query_params
        return args

    async def _aget_tweet_counts_oapg(
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
        Full archive search counts
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_query,
            request_query_start_time,
            request_query_end_time,
            request_query_since_id,
            request_query_until_id,
            request_query_next_token,
            request_query_pagination_token,
            request_query_granularity,
            request_query_search_count_fields,
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
            path_template='/2/tweets/counts/all',
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


    def _get_tweet_counts_oapg(
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
        Full archive search counts
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_query,
            request_query_start_time,
            request_query_end_time,
            request_query_since_id,
            request_query_until_id,
            request_query_next_token,
            request_query_pagination_token,
            request_query_granularity,
            request_query_search_count_fields,
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
            path_template='/2/tweets/counts/all',
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


class GetTweetCountsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_tweet_counts(
        self,
        query: str,
        start_time: typing.Optional[datetime] = None,
        end_time: typing.Optional[datetime] = None,
        since_id: typing.Optional[TweetId] = None,
        until_id: typing.Optional[TweetId] = None,
        next_token: typing.Optional[PaginationToken36] = None,
        pagination_token: typing.Optional[PaginationToken36] = None,
        granularity: typing.Optional[str] = None,
        search_count_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_tweet_counts_mapped_args(
            query=query,
            start_time=start_time,
            end_time=end_time,
            since_id=since_id,
            until_id=until_id,
            next_token=next_token,
            pagination_token=pagination_token,
            granularity=granularity,
            search_count_fields=search_count_fields,
        )
        return await self._aget_tweet_counts_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_tweet_counts(
        self,
        query: str,
        start_time: typing.Optional[datetime] = None,
        end_time: typing.Optional[datetime] = None,
        since_id: typing.Optional[TweetId] = None,
        until_id: typing.Optional[TweetId] = None,
        next_token: typing.Optional[PaginationToken36] = None,
        pagination_token: typing.Optional[PaginationToken36] = None,
        granularity: typing.Optional[str] = None,
        search_count_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_tweet_counts_mapped_args(
            query=query,
            start_time=start_time,
            end_time=end_time,
            since_id=since_id,
            until_id=until_id,
            next_token=next_token,
            pagination_token=pagination_token,
            granularity=granularity,
            search_count_fields=search_count_fields,
        )
        return self._get_tweet_counts_oapg(
            query_params=args.query,
        )

class GetTweetCounts(BaseApi):

    async def aget_tweet_counts(
        self,
        query: str,
        start_time: typing.Optional[datetime] = None,
        end_time: typing.Optional[datetime] = None,
        since_id: typing.Optional[TweetId] = None,
        until_id: typing.Optional[TweetId] = None,
        next_token: typing.Optional[PaginationToken36] = None,
        pagination_token: typing.Optional[PaginationToken36] = None,
        granularity: typing.Optional[str] = None,
        search_count_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> Get2TweetsCountsAllResponsePydantic:
        raw_response = await self.raw.aget_tweet_counts(
            query=query,
            start_time=start_time,
            end_time=end_time,
            since_id=since_id,
            until_id=until_id,
            next_token=next_token,
            pagination_token=pagination_token,
            granularity=granularity,
            search_count_fields=search_count_fields,
            **kwargs,
        )
        if validate:
            return Get2TweetsCountsAllResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(Get2TweetsCountsAllResponsePydantic, raw_response.body)
    
    
    def get_tweet_counts(
        self,
        query: str,
        start_time: typing.Optional[datetime] = None,
        end_time: typing.Optional[datetime] = None,
        since_id: typing.Optional[TweetId] = None,
        until_id: typing.Optional[TweetId] = None,
        next_token: typing.Optional[PaginationToken36] = None,
        pagination_token: typing.Optional[PaginationToken36] = None,
        granularity: typing.Optional[str] = None,
        search_count_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> Get2TweetsCountsAllResponsePydantic:
        raw_response = self.raw.get_tweet_counts(
            query=query,
            start_time=start_time,
            end_time=end_time,
            since_id=since_id,
            until_id=until_id,
            next_token=next_token,
            pagination_token=pagination_token,
            granularity=granularity,
            search_count_fields=search_count_fields,
        )
        if validate:
            return Get2TweetsCountsAllResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(Get2TweetsCountsAllResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        query: str,
        start_time: typing.Optional[datetime] = None,
        end_time: typing.Optional[datetime] = None,
        since_id: typing.Optional[TweetId] = None,
        until_id: typing.Optional[TweetId] = None,
        next_token: typing.Optional[PaginationToken36] = None,
        pagination_token: typing.Optional[PaginationToken36] = None,
        granularity: typing.Optional[str] = None,
        search_count_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_tweet_counts_mapped_args(
            query=query,
            start_time=start_time,
            end_time=end_time,
            since_id=since_id,
            until_id=until_id,
            next_token=next_token,
            pagination_token=pagination_token,
            granularity=granularity,
            search_count_fields=search_count_fields,
        )
        return await self._aget_tweet_counts_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        query: str,
        start_time: typing.Optional[datetime] = None,
        end_time: typing.Optional[datetime] = None,
        since_id: typing.Optional[TweetId] = None,
        until_id: typing.Optional[TweetId] = None,
        next_token: typing.Optional[PaginationToken36] = None,
        pagination_token: typing.Optional[PaginationToken36] = None,
        granularity: typing.Optional[str] = None,
        search_count_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_tweet_counts_mapped_args(
            query=query,
            start_time=start_time,
            end_time=end_time,
            since_id=since_id,
            until_id=until_id,
            next_token=next_token,
            pagination_token=pagination_token,
            granularity=granularity,
            search_count_fields=search_count_fields,
        )
        return self._get_tweet_counts_oapg(
            query_params=args.query,
        )

