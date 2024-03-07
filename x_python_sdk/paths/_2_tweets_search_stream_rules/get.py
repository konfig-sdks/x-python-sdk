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

from x_python_sdk.model.rule_id import RuleId as RuleIdSchema
from x_python_sdk.model.problem import Problem as ProblemSchema
from x_python_sdk.model.rules_lookup_response import RulesLookupResponse as RulesLookupResponseSchema
from x_python_sdk.model.error import Error as ErrorSchema

from x_python_sdk.type.rule_id import RuleId
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.rules_lookup_response import RulesLookupResponse
from x_python_sdk.type.error import Error

from ...api_client import Dictionary
from x_python_sdk.pydantic.error import Error as ErrorPydantic
from x_python_sdk.pydantic.rules_lookup_response import RulesLookupResponse as RulesLookupResponsePydantic
from x_python_sdk.pydantic.problem import Problem as ProblemPydantic
from x_python_sdk.pydantic.rule_id import RuleId as RuleIdPydantic

from . import path

# Query params


class IdsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['RuleId']:
            return RuleId

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['RuleId'], typing.List['RuleId']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IdsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'RuleId':
        return super().__getitem__(i)


class MaxResultsSchema(
    schemas.Int32Schema
):


    class MetaOapg:
        format = 'int32'
        inclusive_maximum = 1000
        inclusive_minimum = 1


class PaginationTokenSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 16
        min_length = 16
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'ids': typing.Union[IdsSchema, list, tuple, ],
        'max_results': typing.Union[MaxResultsSchema, decimal.Decimal, int, ],
        'pagination_token': typing.Union[PaginationTokenSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_ids = api_client.QueryParameter(
    name="ids",
    style=api_client.ParameterStyle.FORM,
    schema=IdsSchema,
    explode=True,
)
request_query_max_results = api_client.QueryParameter(
    name="max_results",
    style=api_client.ParameterStyle.FORM,
    schema=MaxResultsSchema,
    explode=True,
)
request_query_pagination_token = api_client.QueryParameter(
    name="pagination_token",
    style=api_client.ParameterStyle.FORM,
    schema=PaginationTokenSchema,
    explode=True,
)
_auth = [
    'BearerToken',
]
SchemaFor200ResponseBodyApplicationJson = RulesLookupResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: RulesLookupResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: RulesLookupResponse


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

    def _search_stream_rules_mapped_args(
        self,
        ids: typing.Optional[typing.List[RuleId]] = None,
        max_results: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if ids is not None:
            _query_params["ids"] = ids
        if max_results is not None:
            _query_params["max_results"] = max_results
        if pagination_token is not None:
            _query_params["pagination_token"] = pagination_token
        args.query = _query_params
        return args

    async def _asearch_stream_rules_oapg(
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
        Rules lookup
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_ids,
            request_query_max_results,
            request_query_pagination_token,
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
            path_template='/2/tweets/search/stream/rules',
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


    def _search_stream_rules_oapg(
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
        Rules lookup
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_ids,
            request_query_max_results,
            request_query_pagination_token,
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
            path_template='/2/tweets/search/stream/rules',
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


class SearchStreamRulesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asearch_stream_rules(
        self,
        ids: typing.Optional[typing.List[RuleId]] = None,
        max_results: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_stream_rules_mapped_args(
            ids=ids,
            max_results=max_results,
            pagination_token=pagination_token,
        )
        return await self._asearch_stream_rules_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def search_stream_rules(
        self,
        ids: typing.Optional[typing.List[RuleId]] = None,
        max_results: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_stream_rules_mapped_args(
            ids=ids,
            max_results=max_results,
            pagination_token=pagination_token,
        )
        return self._search_stream_rules_oapg(
            query_params=args.query,
        )

class SearchStreamRules(BaseApi):

    async def asearch_stream_rules(
        self,
        ids: typing.Optional[typing.List[RuleId]] = None,
        max_results: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> RulesLookupResponsePydantic:
        raw_response = await self.raw.asearch_stream_rules(
            ids=ids,
            max_results=max_results,
            pagination_token=pagination_token,
            **kwargs,
        )
        if validate:
            return RulesLookupResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(RulesLookupResponsePydantic, raw_response.body)
    
    
    def search_stream_rules(
        self,
        ids: typing.Optional[typing.List[RuleId]] = None,
        max_results: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
        validate: bool = False,
    ) -> RulesLookupResponsePydantic:
        raw_response = self.raw.search_stream_rules(
            ids=ids,
            max_results=max_results,
            pagination_token=pagination_token,
        )
        if validate:
            return RulesLookupResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(RulesLookupResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        ids: typing.Optional[typing.List[RuleId]] = None,
        max_results: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_stream_rules_mapped_args(
            ids=ids,
            max_results=max_results,
            pagination_token=pagination_token,
        )
        return await self._asearch_stream_rules_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        ids: typing.Optional[typing.List[RuleId]] = None,
        max_results: typing.Optional[int] = None,
        pagination_token: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_stream_rules_mapped_args(
            ids=ids,
            max_results=max_results,
            pagination_token=pagination_token,
        )
        return self._search_stream_rules_oapg(
            query_params=args.query,
        )

