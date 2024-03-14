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

from x_python_sdk.model.dm_attachments import DmAttachments as DmAttachmentsSchema
from x_python_sdk.model.create_message_request import CreateMessageRequest as CreateMessageRequestSchema
from x_python_sdk.model.problem import Problem as ProblemSchema
from x_python_sdk.model.create_dm_event_response import CreateDmEventResponse as CreateDmEventResponseSchema
from x_python_sdk.model.error import Error as ErrorSchema
from x_python_sdk.model.user_id import UserId as UserIdSchema

from x_python_sdk.type.create_message_request import CreateMessageRequest
from x_python_sdk.type.dm_attachments import DmAttachments
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.create_dm_event_response import CreateDmEventResponse
from x_python_sdk.type.user_id import UserId
from x_python_sdk.type.error import Error

from ...api_client import Dictionary
from x_python_sdk.pydantic.create_dm_event_response import CreateDmEventResponse as CreateDmEventResponsePydantic
from x_python_sdk.pydantic.dm_attachments import DmAttachments as DmAttachmentsPydantic
from x_python_sdk.pydantic.error import Error as ErrorPydantic
from x_python_sdk.pydantic.create_message_request import CreateMessageRequest as CreateMessageRequestPydantic
from x_python_sdk.pydantic.problem import Problem as ProblemPydantic
from x_python_sdk.pydantic.user_id import UserId as UserIdPydantic

# Path params
ParticipantIdSchema = schemas.Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'participant_id': typing.Union[UserIdSchema, ],
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


request_path_participant_id = api_client.PathParameter(
    name="participant_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UserIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = CreateMessageRequestSchema


request_body_create_message_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = CreateDmEventResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: CreateDmEventResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: CreateDmEventResponse


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
_all_accept_content_types = (
    'application/json',
    'application/problem+json',
)


class BaseApi(api_client.Api):

    def _send_new_message_to_user_mapped_args(
        self,
        participant_id: UserId,
        attachments: typing.Optional[DmAttachments] = None,
        text: typing.Optional[str] = None,
        body: typing.Optional[CreateMessageRequest] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if attachments is not None:
            _body["attachments"] = attachments
        if text is not None:
            _body["text"] = text
        args.body = body if body is not None else _body
        if participant_id is not None:
            _path_params["participant_id"] = participant_id
        args.path = _path_params
        return args

    async def _asend_new_message_to_user_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Send a new message to a user
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_participant_id,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/2/dm_conversations/with/{participant_id}/messages',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_message_request.serialize(body, content_type)
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


    def _send_new_message_to_user_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Send a new message to a user
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_participant_id,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/2/dm_conversations/with/{participant_id}/messages',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_message_request.serialize(body, content_type)
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


class SendNewMessageToUserRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asend_new_message_to_user(
        self,
        participant_id: UserId,
        attachments: typing.Optional[DmAttachments] = None,
        text: typing.Optional[str] = None,
        body: typing.Optional[CreateMessageRequest] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._send_new_message_to_user_mapped_args(
            body=body,
            participant_id=participant_id,
            attachments=attachments,
            text=text,
        )
        return await self._asend_new_message_to_user_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def send_new_message_to_user(
        self,
        participant_id: UserId,
        attachments: typing.Optional[DmAttachments] = None,
        text: typing.Optional[str] = None,
        body: typing.Optional[CreateMessageRequest] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._send_new_message_to_user_mapped_args(
            body=body,
            participant_id=participant_id,
            attachments=attachments,
            text=text,
        )
        return self._send_new_message_to_user_oapg(
            body=args.body,
            path_params=args.path,
        )

class SendNewMessageToUser(BaseApi):

    async def asend_new_message_to_user(
        self,
        participant_id: UserId,
        attachments: typing.Optional[DmAttachments] = None,
        text: typing.Optional[str] = None,
        body: typing.Optional[CreateMessageRequest] = None,
        validate: bool = False,
        **kwargs,
    ) -> CreateDmEventResponsePydantic:
        raw_response = await self.raw.asend_new_message_to_user(
            body=body,
            participant_id=participant_id,
            attachments=attachments,
            text=text,
            **kwargs,
        )
        if validate:
            return CreateDmEventResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CreateDmEventResponsePydantic, raw_response.body)
    
    
    def send_new_message_to_user(
        self,
        participant_id: UserId,
        attachments: typing.Optional[DmAttachments] = None,
        text: typing.Optional[str] = None,
        body: typing.Optional[CreateMessageRequest] = None,
        validate: bool = False,
    ) -> CreateDmEventResponsePydantic:
        raw_response = self.raw.send_new_message_to_user(
            body=body,
            participant_id=participant_id,
            attachments=attachments,
            text=text,
        )
        if validate:
            return CreateDmEventResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CreateDmEventResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        participant_id: UserId,
        attachments: typing.Optional[DmAttachments] = None,
        text: typing.Optional[str] = None,
        body: typing.Optional[CreateMessageRequest] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._send_new_message_to_user_mapped_args(
            body=body,
            participant_id=participant_id,
            attachments=attachments,
            text=text,
        )
        return await self._asend_new_message_to_user_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        participant_id: UserId,
        attachments: typing.Optional[DmAttachments] = None,
        text: typing.Optional[str] = None,
        body: typing.Optional[CreateMessageRequest] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._send_new_message_to_user_mapped_args(
            body=body,
            participant_id=participant_id,
            attachments=attachments,
            text=text,
        )
        return self._send_new_message_to_user_oapg(
            body=args.body,
            path_params=args.path,
        )

