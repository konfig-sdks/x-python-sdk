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

from x_python_sdk.model.get2_compliance_jobs_response import Get2ComplianceJobsResponse as Get2ComplianceJobsResponseSchema
from x_python_sdk.model.problem import Problem as ProblemSchema
from x_python_sdk.model.error import Error as ErrorSchema

from x_python_sdk.type.problem import Problem
from x_python_sdk.type.get2_compliance_jobs_response import Get2ComplianceJobsResponse
from x_python_sdk.type.error import Error

from ...api_client import Dictionary
from x_python_sdk.pydantic.error import Error as ErrorPydantic
from x_python_sdk.pydantic.problem import Problem as ProblemPydantic
from x_python_sdk.pydantic.get2_compliance_jobs_response import Get2ComplianceJobsResponse as Get2ComplianceJobsResponsePydantic

# Query params


class TypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def TWEETS(cls):
        return cls("tweets")
    
    @schemas.classproperty
    def USERS(cls):
        return cls("users")


class StatusSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def CREATED(cls):
        return cls("created")
    
    @schemas.classproperty
    def IN_PROGRESS(cls):
        return cls("in_progress")
    
    @schemas.classproperty
    def FAILED(cls):
        return cls("failed")
    
    @schemas.classproperty
    def COMPLETE(cls):
        return cls("complete")


class ComplianceJobFieldsSchema(
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
            def DOWNLOAD_EXPIRES_AT(cls):
                return cls("download_expires_at")
            
            @schemas.classproperty
            def DOWNLOAD_URL(cls):
                return cls("download_url")
            
            @schemas.classproperty
            def ID(cls):
                return cls("id")
            
            @schemas.classproperty
            def NAME(cls):
                return cls("name")
            
            @schemas.classproperty
            def RESUMABLE(cls):
                return cls("resumable")
            
            @schemas.classproperty
            def STATUS(cls):
                return cls("status")
            
            @schemas.classproperty
            def TYPE(cls):
                return cls("type")
            
            @schemas.classproperty
            def UPLOAD_EXPIRES_AT(cls):
                return cls("upload_expires_at")
            
            @schemas.classproperty
            def UPLOAD_URL(cls):
                return cls("upload_url")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ComplianceJobFieldsSchema':
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
        'type': typing.Union[TypeSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'status': typing.Union[StatusSchema, str, ],
        'compliance_job.fields': typing.Union[ComplianceJobFieldsSchema, list, tuple, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_type = api_client.QueryParameter(
    name="type",
    style=api_client.ParameterStyle.FORM,
    schema=TypeSchema,
    required=True,
    explode=True,
)
request_query_status = api_client.QueryParameter(
    name="status",
    style=api_client.ParameterStyle.FORM,
    schema=StatusSchema,
    explode=True,
)
request_query_compliance_job_fields = api_client.QueryParameter(
    name="compliance_job.fields",
    style=api_client.ParameterStyle.FORM,
    schema=ComplianceJobFieldsSchema,
)
SchemaFor200ResponseBodyApplicationJson = Get2ComplianceJobsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Get2ComplianceJobsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Get2ComplianceJobsResponse


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

    def _list_jobs_mapped_args(
        self,
        type: str,
        status: typing.Optional[str] = None,
        compliance_job_fields: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if type is not None:
            _query_params["type"] = type
        if status is not None:
            _query_params["status"] = status
        if compliance_job_fields is not None:
            _query_params["compliance_job.fields"] = compliance_job_fields
        args.query = _query_params
        return args

    async def _alist_jobs_oapg(
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
        List Compliance Jobs
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_type,
            request_query_status,
            request_query_compliance_job_fields,
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
            path_template='/2/compliance/jobs',
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


    def _list_jobs_oapg(
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
        List Compliance Jobs
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_type,
            request_query_status,
            request_query_compliance_job_fields,
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
            path_template='/2/compliance/jobs',
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


class ListJobsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_jobs(
        self,
        type: str,
        status: typing.Optional[str] = None,
        compliance_job_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_jobs_mapped_args(
            type=type,
            status=status,
            compliance_job_fields=compliance_job_fields,
        )
        return await self._alist_jobs_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_jobs(
        self,
        type: str,
        status: typing.Optional[str] = None,
        compliance_job_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_jobs_mapped_args(
            type=type,
            status=status,
            compliance_job_fields=compliance_job_fields,
        )
        return self._list_jobs_oapg(
            query_params=args.query,
        )

class ListJobs(BaseApi):

    async def alist_jobs(
        self,
        type: str,
        status: typing.Optional[str] = None,
        compliance_job_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> Get2ComplianceJobsResponsePydantic:
        raw_response = await self.raw.alist_jobs(
            type=type,
            status=status,
            compliance_job_fields=compliance_job_fields,
            **kwargs,
        )
        if validate:
            return Get2ComplianceJobsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(Get2ComplianceJobsResponsePydantic, raw_response.body)
    
    
    def list_jobs(
        self,
        type: str,
        status: typing.Optional[str] = None,
        compliance_job_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> Get2ComplianceJobsResponsePydantic:
        raw_response = self.raw.list_jobs(
            type=type,
            status=status,
            compliance_job_fields=compliance_job_fields,
        )
        if validate:
            return Get2ComplianceJobsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(Get2ComplianceJobsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        type: str,
        status: typing.Optional[str] = None,
        compliance_job_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_jobs_mapped_args(
            type=type,
            status=status,
            compliance_job_fields=compliance_job_fields,
        )
        return await self._alist_jobs_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        type: str,
        status: typing.Optional[str] = None,
        compliance_job_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_jobs_mapped_args(
            type=type,
            status=status,
            compliance_job_fields=compliance_job_fields,
        )
        return self._list_jobs_oapg(
            query_params=args.query,
        )

