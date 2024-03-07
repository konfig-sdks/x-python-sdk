# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.62
    Created by: https://developer.twitter.com/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from x_python_sdk.pydantic.compliance_job_name import ComplianceJobName
from x_python_sdk.pydantic.compliance_job_status import ComplianceJobStatus
from x_python_sdk.pydantic.compliance_job_type import ComplianceJobType
from x_python_sdk.pydantic.job_id import JobId

class ComplianceJob(BaseModel):
    # Creation time of the compliance job.
    created_at: datetime = Field(alias='created_at')

    # Expiration time of the download URL.
    download_expires_at: datetime = Field(alias='download_expires_at')

    # URL from which the user will retrieve their compliance results.
    download_url: str = Field(alias='download_url')

    id: JobId = Field(alias='id')

    status: ComplianceJobStatus = Field(alias='status')

    type: ComplianceJobType = Field(alias='type')

    # Expiration time of the upload URL.
    upload_expires_at: datetime = Field(alias='upload_expires_at')

    # URL to which the user will upload their Tweet or user IDs.
    upload_url: str = Field(alias='upload_url')

    name: typing.Optional[ComplianceJobName] = Field(None, alias='name')
    class Config:
        arbitrary_types_allowed = True
