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
from x_python_sdk.model.tweet_create_request_geo import TweetCreateRequestGeo as TweetCreateRequestGeoSchema
from x_python_sdk.model.tweet_create_request_poll import TweetCreateRequestPoll as TweetCreateRequestPollSchema
from x_python_sdk.model.problem import Problem as ProblemSchema
from x_python_sdk.model.tweet_create_response import TweetCreateResponse as TweetCreateResponseSchema
from x_python_sdk.model.error import Error as ErrorSchema
from x_python_sdk.model.tweet_create_request import TweetCreateRequest as TweetCreateRequestSchema
from x_python_sdk.model.tweet_create_request_reply import TweetCreateRequestReply as TweetCreateRequestReplySchema
from x_python_sdk.model.tweet_create_request_media import TweetCreateRequestMedia as TweetCreateRequestMediaSchema

from x_python_sdk.type.tweet_create_request_geo import TweetCreateRequestGeo
from x_python_sdk.type.tweet_create_response import TweetCreateResponse
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.tweet_create_request import TweetCreateRequest
from x_python_sdk.type.tweet_create_request_poll import TweetCreateRequestPoll
from x_python_sdk.type.tweet_create_request_media import TweetCreateRequestMedia
from x_python_sdk.type.tweet_create_request_reply import TweetCreateRequestReply
from x_python_sdk.type.error import Error
from x_python_sdk.type.tweet_id import TweetId

from ...api_client import Dictionary
from x_python_sdk.pydantic.tweet_create_request_geo import TweetCreateRequestGeo as TweetCreateRequestGeoPydantic
from x_python_sdk.pydantic.error import Error as ErrorPydantic
from x_python_sdk.pydantic.tweet_create_request import TweetCreateRequest as TweetCreateRequestPydantic
from x_python_sdk.pydantic.problem import Problem as ProblemPydantic
from x_python_sdk.pydantic.tweet_create_request_media import TweetCreateRequestMedia as TweetCreateRequestMediaPydantic
from x_python_sdk.pydantic.tweet_create_response import TweetCreateResponse as TweetCreateResponsePydantic
from x_python_sdk.pydantic.tweet_create_request_reply import TweetCreateRequestReply as TweetCreateRequestReplyPydantic
from x_python_sdk.pydantic.tweet_create_request_poll import TweetCreateRequestPoll as TweetCreateRequestPollPydantic
from x_python_sdk.pydantic.tweet_id import TweetId as TweetIdPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = TweetCreateRequestSchema


request_body_tweet_create_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'OAuth2UserToken',
    'UserToken',
]
SchemaFor201ResponseBodyApplicationJson = TweetCreateResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: TweetCreateResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: TweetCreateResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
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
    '201': _response_for_201,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
    'application/problem+json',
)


class BaseApi(api_client.Api):

    def _create_tweet_mapped_args(
        self,
        card_uri: typing.Optional[str] = None,
        direct_message_deep_link: typing.Optional[str] = None,
        for_super_followers_only: typing.Optional[bool] = None,
        geo: typing.Optional[TweetCreateRequestGeo] = None,
        media: typing.Optional[TweetCreateRequestMedia] = None,
        nullcast: typing.Optional[bool] = None,
        poll: typing.Optional[TweetCreateRequestPoll] = None,
        quote_tweet_id: typing.Optional[TweetId] = None,
        reply: typing.Optional[TweetCreateRequestReply] = None,
        reply_settings: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if card_uri is not None:
            _body["card_uri"] = card_uri
        if direct_message_deep_link is not None:
            _body["direct_message_deep_link"] = direct_message_deep_link
        if for_super_followers_only is not None:
            _body["for_super_followers_only"] = for_super_followers_only
        if geo is not None:
            _body["geo"] = geo
        if media is not None:
            _body["media"] = media
        if nullcast is not None:
            _body["nullcast"] = nullcast
        if poll is not None:
            _body["poll"] = poll
        if quote_tweet_id is not None:
            _body["quote_tweet_id"] = quote_tweet_id
        if reply is not None:
            _body["reply"] = reply
        if reply_settings is not None:
            _body["reply_settings"] = reply_settings
        if text is not None:
            _body["text"] = text
        args.body = _body
        return args

    async def _acreate_tweet_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Creation of a Tweet
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/2/tweets',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_tweet_create_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _create_tweet_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Creation of a Tweet
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/2/tweets',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_tweet_create_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class CreateTweetRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_tweet(
        self,
        card_uri: typing.Optional[str] = None,
        direct_message_deep_link: typing.Optional[str] = None,
        for_super_followers_only: typing.Optional[bool] = None,
        geo: typing.Optional[TweetCreateRequestGeo] = None,
        media: typing.Optional[TweetCreateRequestMedia] = None,
        nullcast: typing.Optional[bool] = None,
        poll: typing.Optional[TweetCreateRequestPoll] = None,
        quote_tweet_id: typing.Optional[TweetId] = None,
        reply: typing.Optional[TweetCreateRequestReply] = None,
        reply_settings: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_tweet_mapped_args(
            card_uri=card_uri,
            direct_message_deep_link=direct_message_deep_link,
            for_super_followers_only=for_super_followers_only,
            geo=geo,
            media=media,
            nullcast=nullcast,
            poll=poll,
            quote_tweet_id=quote_tweet_id,
            reply=reply,
            reply_settings=reply_settings,
            text=text,
        )
        return await self._acreate_tweet_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_tweet(
        self,
        card_uri: typing.Optional[str] = None,
        direct_message_deep_link: typing.Optional[str] = None,
        for_super_followers_only: typing.Optional[bool] = None,
        geo: typing.Optional[TweetCreateRequestGeo] = None,
        media: typing.Optional[TweetCreateRequestMedia] = None,
        nullcast: typing.Optional[bool] = None,
        poll: typing.Optional[TweetCreateRequestPoll] = None,
        quote_tweet_id: typing.Optional[TweetId] = None,
        reply: typing.Optional[TweetCreateRequestReply] = None,
        reply_settings: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_tweet_mapped_args(
            card_uri=card_uri,
            direct_message_deep_link=direct_message_deep_link,
            for_super_followers_only=for_super_followers_only,
            geo=geo,
            media=media,
            nullcast=nullcast,
            poll=poll,
            quote_tweet_id=quote_tweet_id,
            reply=reply,
            reply_settings=reply_settings,
            text=text,
        )
        return self._create_tweet_oapg(
            body=args.body,
        )

class CreateTweet(BaseApi):

    async def acreate_tweet(
        self,
        card_uri: typing.Optional[str] = None,
        direct_message_deep_link: typing.Optional[str] = None,
        for_super_followers_only: typing.Optional[bool] = None,
        geo: typing.Optional[TweetCreateRequestGeo] = None,
        media: typing.Optional[TweetCreateRequestMedia] = None,
        nullcast: typing.Optional[bool] = None,
        poll: typing.Optional[TweetCreateRequestPoll] = None,
        quote_tweet_id: typing.Optional[TweetId] = None,
        reply: typing.Optional[TweetCreateRequestReply] = None,
        reply_settings: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> TweetCreateResponsePydantic:
        raw_response = await self.raw.acreate_tweet(
            card_uri=card_uri,
            direct_message_deep_link=direct_message_deep_link,
            for_super_followers_only=for_super_followers_only,
            geo=geo,
            media=media,
            nullcast=nullcast,
            poll=poll,
            quote_tweet_id=quote_tweet_id,
            reply=reply,
            reply_settings=reply_settings,
            text=text,
            **kwargs,
        )
        if validate:
            return TweetCreateResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TweetCreateResponsePydantic, raw_response.body)
    
    
    def create_tweet(
        self,
        card_uri: typing.Optional[str] = None,
        direct_message_deep_link: typing.Optional[str] = None,
        for_super_followers_only: typing.Optional[bool] = None,
        geo: typing.Optional[TweetCreateRequestGeo] = None,
        media: typing.Optional[TweetCreateRequestMedia] = None,
        nullcast: typing.Optional[bool] = None,
        poll: typing.Optional[TweetCreateRequestPoll] = None,
        quote_tweet_id: typing.Optional[TweetId] = None,
        reply: typing.Optional[TweetCreateRequestReply] = None,
        reply_settings: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        validate: bool = False,
    ) -> TweetCreateResponsePydantic:
        raw_response = self.raw.create_tweet(
            card_uri=card_uri,
            direct_message_deep_link=direct_message_deep_link,
            for_super_followers_only=for_super_followers_only,
            geo=geo,
            media=media,
            nullcast=nullcast,
            poll=poll,
            quote_tweet_id=quote_tweet_id,
            reply=reply,
            reply_settings=reply_settings,
            text=text,
        )
        if validate:
            return TweetCreateResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TweetCreateResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        card_uri: typing.Optional[str] = None,
        direct_message_deep_link: typing.Optional[str] = None,
        for_super_followers_only: typing.Optional[bool] = None,
        geo: typing.Optional[TweetCreateRequestGeo] = None,
        media: typing.Optional[TweetCreateRequestMedia] = None,
        nullcast: typing.Optional[bool] = None,
        poll: typing.Optional[TweetCreateRequestPoll] = None,
        quote_tweet_id: typing.Optional[TweetId] = None,
        reply: typing.Optional[TweetCreateRequestReply] = None,
        reply_settings: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_tweet_mapped_args(
            card_uri=card_uri,
            direct_message_deep_link=direct_message_deep_link,
            for_super_followers_only=for_super_followers_only,
            geo=geo,
            media=media,
            nullcast=nullcast,
            poll=poll,
            quote_tweet_id=quote_tweet_id,
            reply=reply,
            reply_settings=reply_settings,
            text=text,
        )
        return await self._acreate_tweet_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        card_uri: typing.Optional[str] = None,
        direct_message_deep_link: typing.Optional[str] = None,
        for_super_followers_only: typing.Optional[bool] = None,
        geo: typing.Optional[TweetCreateRequestGeo] = None,
        media: typing.Optional[TweetCreateRequestMedia] = None,
        nullcast: typing.Optional[bool] = None,
        poll: typing.Optional[TweetCreateRequestPoll] = None,
        quote_tweet_id: typing.Optional[TweetId] = None,
        reply: typing.Optional[TweetCreateRequestReply] = None,
        reply_settings: typing.Optional[str] = None,
        text: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_tweet_mapped_args(
            card_uri=card_uri,
            direct_message_deep_link=direct_message_deep_link,
            for_super_followers_only=for_super_followers_only,
            geo=geo,
            media=media,
            nullcast=nullcast,
            poll=poll,
            quote_tweet_id=quote_tweet_id,
            reply=reply,
            reply_settings=reply_settings,
            text=text,
        )
        return self._create_tweet_oapg(
            body=args.body,
        )

