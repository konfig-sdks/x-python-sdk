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
from x_python_sdk.model.bookmark_mutation_response import BookmarkMutationResponse as BookmarkMutationResponseSchema
from x_python_sdk.model.problem import Problem as ProblemSchema
from x_python_sdk.model.error import Error as ErrorSchema

from x_python_sdk.type.bookmark_mutation_response import BookmarkMutationResponse
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.error import Error
from x_python_sdk.type.tweet_id import TweetId

from ...api_client import Dictionary
from x_python_sdk.pydantic.error import Error as ErrorPydantic
from x_python_sdk.pydantic.bookmark_mutation_response import BookmarkMutationResponse as BookmarkMutationResponsePydantic
from x_python_sdk.pydantic.problem import Problem as ProblemPydantic
from x_python_sdk.pydantic.tweet_id import TweetId as TweetIdPydantic

# Path params
IdSchema = schemas.StrSchema
TweetIdSchema = schemas.Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'id': typing.Union[IdSchema, str, ],
        'tweet_id': typing.Union[TweetId, ],
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
request_path_tweet_id = api_client.PathParameter(
    name="tweet_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TweetId,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = BookmarkMutationResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: BookmarkMutationResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: BookmarkMutationResponse


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

    def _remove_tweet_mapped_args(
        self,
        id: str,
        tweet_id: TweetId,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if id is not None:
            _path_params["id"] = id
        if tweet_id is not None:
            _path_params["tweet_id"] = tweet_id
        args.path = _path_params
        return args

    async def _aremove_tweet_oapg(
        self,
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
        Remove a bookmarked Tweet
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
            request_path_tweet_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/2/users/{id}/bookmarks/{tweet_id}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


    def _remove_tweet_oapg(
        self,
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
        Remove a bookmarked Tweet
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
            request_path_tweet_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/2/users/{id}/bookmarks/{tweet_id}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


class RemoveTweetRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aremove_tweet(
        self,
        id: str,
        tweet_id: TweetId,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._remove_tweet_mapped_args(
            id=id,
            tweet_id=tweet_id,
        )
        return await self._aremove_tweet_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def remove_tweet(
        self,
        id: str,
        tweet_id: TweetId,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._remove_tweet_mapped_args(
            id=id,
            tweet_id=tweet_id,
        )
        return self._remove_tweet_oapg(
            path_params=args.path,
        )

class RemoveTweet(BaseApi):

    async def aremove_tweet(
        self,
        id: str,
        tweet_id: TweetId,
        validate: bool = False,
        **kwargs,
    ) -> BookmarkMutationResponsePydantic:
        raw_response = await self.raw.aremove_tweet(
            id=id,
            tweet_id=tweet_id,
            **kwargs,
        )
        if validate:
            return BookmarkMutationResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(BookmarkMutationResponsePydantic, raw_response.body)
    
    
    def remove_tweet(
        self,
        id: str,
        tweet_id: TweetId,
        validate: bool = False,
    ) -> BookmarkMutationResponsePydantic:
        raw_response = self.raw.remove_tweet(
            id=id,
            tweet_id=tweet_id,
        )
        if validate:
            return BookmarkMutationResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(BookmarkMutationResponsePydantic, raw_response.body)


class ApiFordelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def adelete(
        self,
        id: str,
        tweet_id: TweetId,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._remove_tweet_mapped_args(
            id=id,
            tweet_id=tweet_id,
        )
        return await self._aremove_tweet_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def delete(
        self,
        id: str,
        tweet_id: TweetId,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._remove_tweet_mapped_args(
            id=id,
            tweet_id=tweet_id,
        )
        return self._remove_tweet_oapg(
            path_params=args.path,
        )

