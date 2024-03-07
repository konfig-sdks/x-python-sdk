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
from x_python_sdk.model.get2_spaces_search_response import Get2SpacesSearchResponse as Get2SpacesSearchResponseSchema
from x_python_sdk.model.error import Error as ErrorSchema

from x_python_sdk.type.get2_spaces_search_response import Get2SpacesSearchResponse
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.error import Error

from ...api_client import Dictionary
from x_python_sdk.pydantic.error import Error as ErrorPydantic
from x_python_sdk.pydantic.problem import Problem as ProblemPydantic
from x_python_sdk.pydantic.get2_spaces_search_response import Get2SpacesSearchResponse as Get2SpacesSearchResponsePydantic

# Query params


class QuerySchema(
    schemas.StrSchema
):
    pass


class StateSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def LIVE(cls):
        return cls("live")
    
    @schemas.classproperty
    def SCHEDULED(cls):
        return cls("scheduled")
    
    @schemas.classproperty
    def ALL(cls):
        return cls("all")


class MaxResultsSchema(
    schemas.Int32Schema
):
    pass


class SpaceFieldsSchema(
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
            def CREATOR_ID(cls):
                return cls("creator_id")
            
            @schemas.classproperty
            def ENDED_AT(cls):
                return cls("ended_at")
            
            @schemas.classproperty
            def HOST_IDS(cls):
                return cls("host_ids")
            
            @schemas.classproperty
            def ID(cls):
                return cls("id")
            
            @schemas.classproperty
            def INVITED_USER_IDS(cls):
                return cls("invited_user_ids")
            
            @schemas.classproperty
            def IS_TICKETED(cls):
                return cls("is_ticketed")
            
            @schemas.classproperty
            def LANG(cls):
                return cls("lang")
            
            @schemas.classproperty
            def PARTICIPANT_COUNT(cls):
                return cls("participant_count")
            
            @schemas.classproperty
            def SCHEDULED_START(cls):
                return cls("scheduled_start")
            
            @schemas.classproperty
            def SPEAKER_IDS(cls):
                return cls("speaker_ids")
            
            @schemas.classproperty
            def STARTED_AT(cls):
                return cls("started_at")
            
            @schemas.classproperty
            def STATE(cls):
                return cls("state")
            
            @schemas.classproperty
            def SUBSCRIBER_COUNT(cls):
                return cls("subscriber_count")
            
            @schemas.classproperty
            def TITLE(cls):
                return cls("title")
            
            @schemas.classproperty
            def TOPIC_IDS(cls):
                return cls("topic_ids")
            
            @schemas.classproperty
            def UPDATED_AT(cls):
                return cls("updated_at")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SpaceFieldsSchema':
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
            def CREATOR_ID(cls):
                return cls("creator_id")
            
            @schemas.classproperty
            def HOST_IDS(cls):
                return cls("host_ids")
            
            @schemas.classproperty
            def INVITED_USER_IDS(cls):
                return cls("invited_user_ids")
            
            @schemas.classproperty
            def SPEAKER_IDS(cls):
                return cls("speaker_ids")
            
            @schemas.classproperty
            def TOPIC_IDS(cls):
                return cls("topic_ids")

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


class TopicFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
            @schemas.classproperty
            def DESCRIPTION(cls):
                return cls("description")
            
            @schemas.classproperty
            def ID(cls):
                return cls("id")
            
            @schemas.classproperty
            def NAME(cls):
                return cls("name")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TopicFieldsSchema':
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
        'state': typing.Union[StateSchema, str, ],
        'max_results': typing.Union[MaxResultsSchema, decimal.Decimal, int, ],
        'space.fields': typing.Union[SpaceFieldsSchema, list, tuple, ],
        'expansions': typing.Union[ExpansionsSchema, list, tuple, ],
        'user.fields': typing.Union[UserFieldsSchema, list, tuple, ],
        'topic.fields': typing.Union[TopicFieldsSchema, list, tuple, ],
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
request_query_state = api_client.QueryParameter(
    name="state",
    style=api_client.ParameterStyle.FORM,
    schema=StateSchema,
    explode=True,
)
request_query_max_results = api_client.QueryParameter(
    name="max_results",
    style=api_client.ParameterStyle.FORM,
    schema=MaxResultsSchema,
    explode=True,
)
request_query_space_fields = api_client.QueryParameter(
    name="space.fields",
    style=api_client.ParameterStyle.FORM,
    schema=SpaceFieldsSchema,
)
request_query_expansions = api_client.QueryParameter(
    name="expansions",
    style=api_client.ParameterStyle.FORM,
    schema=ExpansionsSchema,
)
request_query_user_fields = api_client.QueryParameter(
    name="user.fields",
    style=api_client.ParameterStyle.FORM,
    schema=UserFieldsSchema,
)
request_query_topic_fields = api_client.QueryParameter(
    name="topic.fields",
    style=api_client.ParameterStyle.FORM,
    schema=TopicFieldsSchema,
)
SchemaFor200ResponseBodyApplicationJson = Get2SpacesSearchResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Get2SpacesSearchResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Get2SpacesSearchResponse


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

    def _find_matching_spaces_mapped_args(
        self,
        query: str,
        state: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        space_fields: typing.Optional[typing.List[str]] = None,
        expansions: typing.Optional[typing.List[str]] = None,
        user_fields: typing.Optional[typing.List[str]] = None,
        topic_fields: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if query is not None:
            _query_params["query"] = query
        if state is not None:
            _query_params["state"] = state
        if max_results is not None:
            _query_params["max_results"] = max_results
        if space_fields is not None:
            _query_params["space.fields"] = space_fields
        if expansions is not None:
            _query_params["expansions"] = expansions
        if user_fields is not None:
            _query_params["user.fields"] = user_fields
        if topic_fields is not None:
            _query_params["topic.fields"] = topic_fields
        args.query = _query_params
        return args

    async def _afind_matching_spaces_oapg(
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
        Search for Spaces
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_query,
            request_query_state,
            request_query_max_results,
            request_query_space_fields,
            request_query_expansions,
            request_query_user_fields,
            request_query_topic_fields,
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
            path_template='/2/spaces/search',
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


    def _find_matching_spaces_oapg(
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
        Search for Spaces
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_query,
            request_query_state,
            request_query_max_results,
            request_query_space_fields,
            request_query_expansions,
            request_query_user_fields,
            request_query_topic_fields,
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
            path_template='/2/spaces/search',
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


class FindMatchingSpacesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def afind_matching_spaces(
        self,
        query: str,
        state: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        space_fields: typing.Optional[typing.List[str]] = None,
        expansions: typing.Optional[typing.List[str]] = None,
        user_fields: typing.Optional[typing.List[str]] = None,
        topic_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._find_matching_spaces_mapped_args(
            query=query,
            state=state,
            max_results=max_results,
            space_fields=space_fields,
            expansions=expansions,
            user_fields=user_fields,
            topic_fields=topic_fields,
        )
        return await self._afind_matching_spaces_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def find_matching_spaces(
        self,
        query: str,
        state: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        space_fields: typing.Optional[typing.List[str]] = None,
        expansions: typing.Optional[typing.List[str]] = None,
        user_fields: typing.Optional[typing.List[str]] = None,
        topic_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._find_matching_spaces_mapped_args(
            query=query,
            state=state,
            max_results=max_results,
            space_fields=space_fields,
            expansions=expansions,
            user_fields=user_fields,
            topic_fields=topic_fields,
        )
        return self._find_matching_spaces_oapg(
            query_params=args.query,
        )

class FindMatchingSpaces(BaseApi):

    async def afind_matching_spaces(
        self,
        query: str,
        state: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        space_fields: typing.Optional[typing.List[str]] = None,
        expansions: typing.Optional[typing.List[str]] = None,
        user_fields: typing.Optional[typing.List[str]] = None,
        topic_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> Get2SpacesSearchResponsePydantic:
        raw_response = await self.raw.afind_matching_spaces(
            query=query,
            state=state,
            max_results=max_results,
            space_fields=space_fields,
            expansions=expansions,
            user_fields=user_fields,
            topic_fields=topic_fields,
            **kwargs,
        )
        if validate:
            return Get2SpacesSearchResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(Get2SpacesSearchResponsePydantic, raw_response.body)
    
    
    def find_matching_spaces(
        self,
        query: str,
        state: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        space_fields: typing.Optional[typing.List[str]] = None,
        expansions: typing.Optional[typing.List[str]] = None,
        user_fields: typing.Optional[typing.List[str]] = None,
        topic_fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> Get2SpacesSearchResponsePydantic:
        raw_response = self.raw.find_matching_spaces(
            query=query,
            state=state,
            max_results=max_results,
            space_fields=space_fields,
            expansions=expansions,
            user_fields=user_fields,
            topic_fields=topic_fields,
        )
        if validate:
            return Get2SpacesSearchResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(Get2SpacesSearchResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        query: str,
        state: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        space_fields: typing.Optional[typing.List[str]] = None,
        expansions: typing.Optional[typing.List[str]] = None,
        user_fields: typing.Optional[typing.List[str]] = None,
        topic_fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._find_matching_spaces_mapped_args(
            query=query,
            state=state,
            max_results=max_results,
            space_fields=space_fields,
            expansions=expansions,
            user_fields=user_fields,
            topic_fields=topic_fields,
        )
        return await self._afind_matching_spaces_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        query: str,
        state: typing.Optional[str] = None,
        max_results: typing.Optional[int] = None,
        space_fields: typing.Optional[typing.List[str]] = None,
        expansions: typing.Optional[typing.List[str]] = None,
        user_fields: typing.Optional[typing.List[str]] = None,
        topic_fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._find_matching_spaces_mapped_args(
            query=query,
            state=state,
            max_results=max_results,
            space_fields=space_fields,
            expansions=expansions,
            user_fields=user_fields,
            topic_fields=topic_fields,
        )
        return self._find_matching_spaces_oapg(
            query_params=args.query,
        )

