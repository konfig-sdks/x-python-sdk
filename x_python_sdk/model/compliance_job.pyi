# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.62
    Created by: https://developer.twitter.com/
"""

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


class ComplianceJob(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "download_expires_at",
            "download_url",
            "upload_expires_at",
            "created_at",
            "upload_url",
            "id",
            "type",
            "status",
        }
        
        class properties:
            created_at = schemas.DateTimeSchema
            download_expires_at = schemas.DateTimeSchema
            download_url = schemas.StrSchema
        
            @staticmethod
            def id() -> typing.Type['JobId']:
                return JobId
        
            @staticmethod
            def status() -> typing.Type['ComplianceJobStatus']:
                return ComplianceJobStatus
        
            @staticmethod
            def type() -> typing.Type['ComplianceJobType']:
                return ComplianceJobType
            upload_expires_at = schemas.DateTimeSchema
            upload_url = schemas.StrSchema
        
            @staticmethod
            def name() -> typing.Type['ComplianceJobName']:
                return ComplianceJobName
            __annotations__ = {
                "created_at": created_at,
                "download_expires_at": download_expires_at,
                "download_url": download_url,
                "id": id,
                "status": status,
                "type": type,
                "upload_expires_at": upload_expires_at,
                "upload_url": upload_url,
                "name": name,
            }
    
    download_expires_at: MetaOapg.properties.download_expires_at
    download_url: MetaOapg.properties.download_url
    upload_expires_at: MetaOapg.properties.upload_expires_at
    created_at: MetaOapg.properties.created_at
    upload_url: MetaOapg.properties.upload_url
    id: 'JobId'
    type: 'ComplianceJobType'
    status: 'ComplianceJobStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["download_expires_at"]) -> MetaOapg.properties.download_expires_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["download_url"]) -> MetaOapg.properties.download_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'JobId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'ComplianceJobStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'ComplianceJobType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upload_expires_at"]) -> MetaOapg.properties.upload_expires_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upload_url"]) -> MetaOapg.properties.upload_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> 'ComplianceJobName': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["created_at", "download_expires_at", "download_url", "id", "status", "type", "upload_expires_at", "upload_url", "name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["download_expires_at"]) -> MetaOapg.properties.download_expires_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["download_url"]) -> MetaOapg.properties.download_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'JobId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'ComplianceJobStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'ComplianceJobType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upload_expires_at"]) -> MetaOapg.properties.upload_expires_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upload_url"]) -> MetaOapg.properties.upload_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union['ComplianceJobName', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["created_at", "download_expires_at", "download_url", "id", "status", "type", "upload_expires_at", "upload_url", "name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        download_expires_at: typing.Union[MetaOapg.properties.download_expires_at, str, datetime, ],
        download_url: typing.Union[MetaOapg.properties.download_url, str, ],
        upload_expires_at: typing.Union[MetaOapg.properties.upload_expires_at, str, datetime, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, ],
        upload_url: typing.Union[MetaOapg.properties.upload_url, str, ],
        id: 'JobId',
        type: 'ComplianceJobType',
        status: 'ComplianceJobStatus',
        name: typing.Union['ComplianceJobName', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ComplianceJob':
        return super().__new__(
            cls,
            *args,
            download_expires_at=download_expires_at,
            download_url=download_url,
            upload_expires_at=upload_expires_at,
            created_at=created_at,
            upload_url=upload_url,
            id=id,
            type=type,
            status=status,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.compliance_job_name import ComplianceJobName
from x_python_sdk.model.compliance_job_status import ComplianceJobStatus
from x_python_sdk.model.compliance_job_type import ComplianceJobType
from x_python_sdk.model.job_id import JobId
