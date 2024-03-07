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

from x_python_sdk.model.add_or_delete_rules_request import AddOrDeleteRulesRequest as AddOrDeleteRulesRequestSchema
from x_python_sdk.model.delete_rules_request_delete import DeleteRulesRequestDelete as DeleteRulesRequestDeleteSchema
from x_python_sdk.model.problem import Problem as ProblemSchema
from x_python_sdk.model.add_or_delete_rules_response import AddOrDeleteRulesResponse as AddOrDeleteRulesResponseSchema
from x_python_sdk.model.error import Error as ErrorSchema
from x_python_sdk.model.rule_no_id import RuleNoId as RuleNoIdSchema

from x_python_sdk.type.add_or_delete_rules_request import AddOrDeleteRulesRequest
from x_python_sdk.type.rule_no_id import RuleNoId
from x_python_sdk.type.add_or_delete_rules_response import AddOrDeleteRulesResponse
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.delete_rules_request_delete import DeleteRulesRequestDelete
from x_python_sdk.type.error import Error

from ...api_client import Dictionary
from x_python_sdk.pydantic.error import Error as ErrorPydantic
from x_python_sdk.pydantic.add_or_delete_rules_response import AddOrDeleteRulesResponse as AddOrDeleteRulesResponsePydantic
from x_python_sdk.pydantic.delete_rules_request_delete import DeleteRulesRequestDelete as DeleteRulesRequestDeletePydantic
from x_python_sdk.pydantic.rule_no_id import RuleNoId as RuleNoIdPydantic
from x_python_sdk.pydantic.problem import Problem as ProblemPydantic
from x_python_sdk.pydantic.add_or_delete_rules_request import AddOrDeleteRulesRequest as AddOrDeleteRulesRequestPydantic

from . import path

# Query params
DryRunSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'dry_run': typing.Union[DryRunSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_dry_run = api_client.QueryParameter(
    name="dry_run",
    style=api_client.ParameterStyle.FORM,
    schema=DryRunSchema,
    explode=True,
)
# body param
SchemaForRequestBodyApplicationJson = AddOrDeleteRulesRequestSchema


request_body_add_or_delete_rules_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'BearerToken',
]
SchemaFor200ResponseBodyApplicationJson = AddOrDeleteRulesResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AddOrDeleteRulesResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AddOrDeleteRulesResponse


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

    def _add_or_delete_rules_mapped_args(
        self,
        body: typing.Optional[AddOrDeleteRulesRequest] = None,
        add: typing.Optional[typing.List[RuleNoId]] = None,
        delete: typing.Optional[DeleteRulesRequestDelete] = None,
        dry_run: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if add is not None:
            _body["add"] = add
        if delete is not None:
            _body["delete"] = delete
        args.body = body if body is not None else _body
        if dry_run is not None:
            _query_params["dry_run"] = dry_run
        args.query = _query_params
        return args

    async def _aadd_or_delete_rules_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Add/Delete rules
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_dry_run,
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
            path_template='/2/tweets/search/stream/rules',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_add_or_delete_rules_request.serialize(body, content_type)
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


    def _add_or_delete_rules_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Add/Delete rules
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_dry_run,
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
            path_template='/2/tweets/search/stream/rules',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_add_or_delete_rules_request.serialize(body, content_type)
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


class AddOrDeleteRulesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_or_delete_rules(
        self,
        body: typing.Optional[AddOrDeleteRulesRequest] = None,
        add: typing.Optional[typing.List[RuleNoId]] = None,
        delete: typing.Optional[DeleteRulesRequestDelete] = None,
        dry_run: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_or_delete_rules_mapped_args(
            body=body,
            add=add,
            delete=delete,
            dry_run=dry_run,
        )
        return await self._aadd_or_delete_rules_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def add_or_delete_rules(
        self,
        body: typing.Optional[AddOrDeleteRulesRequest] = None,
        add: typing.Optional[typing.List[RuleNoId]] = None,
        delete: typing.Optional[DeleteRulesRequestDelete] = None,
        dry_run: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_or_delete_rules_mapped_args(
            body=body,
            add=add,
            delete=delete,
            dry_run=dry_run,
        )
        return self._add_or_delete_rules_oapg(
            body=args.body,
            query_params=args.query,
        )

class AddOrDeleteRules(BaseApi):

    async def aadd_or_delete_rules(
        self,
        body: typing.Optional[AddOrDeleteRulesRequest] = None,
        add: typing.Optional[typing.List[RuleNoId]] = None,
        delete: typing.Optional[DeleteRulesRequestDelete] = None,
        dry_run: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> AddOrDeleteRulesResponsePydantic:
        raw_response = await self.raw.aadd_or_delete_rules(
            body=body,
            add=add,
            delete=delete,
            dry_run=dry_run,
            **kwargs,
        )
        if validate:
            return AddOrDeleteRulesResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AddOrDeleteRulesResponsePydantic, raw_response.body)
    
    
    def add_or_delete_rules(
        self,
        body: typing.Optional[AddOrDeleteRulesRequest] = None,
        add: typing.Optional[typing.List[RuleNoId]] = None,
        delete: typing.Optional[DeleteRulesRequestDelete] = None,
        dry_run: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> AddOrDeleteRulesResponsePydantic:
        raw_response = self.raw.add_or_delete_rules(
            body=body,
            add=add,
            delete=delete,
            dry_run=dry_run,
        )
        if validate:
            return AddOrDeleteRulesResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AddOrDeleteRulesResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        body: typing.Optional[AddOrDeleteRulesRequest] = None,
        add: typing.Optional[typing.List[RuleNoId]] = None,
        delete: typing.Optional[DeleteRulesRequestDelete] = None,
        dry_run: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_or_delete_rules_mapped_args(
            body=body,
            add=add,
            delete=delete,
            dry_run=dry_run,
        )
        return await self._aadd_or_delete_rules_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        body: typing.Optional[AddOrDeleteRulesRequest] = None,
        add: typing.Optional[typing.List[RuleNoId]] = None,
        delete: typing.Optional[DeleteRulesRequestDelete] = None,
        dry_run: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_or_delete_rules_mapped_args(
            body=body,
            add=add,
            delete=delete,
            dry_run=dry_run,
        )
        return self._add_or_delete_rules_oapg(
            body=args.body,
            query_params=args.query,
        )

