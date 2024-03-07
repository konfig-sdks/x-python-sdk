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

from x_python_sdk.type.compliance_job_name import ComplianceJobName
from x_python_sdk.type.compliance_job_status import ComplianceJobStatus
from x_python_sdk.type.compliance_job_type import ComplianceJobType
from x_python_sdk.type.job_id import JobId

class RequiredComplianceJob(TypedDict):
    # Creation time of the compliance job.
    created_at: datetime

    # Expiration time of the download URL.
    download_expires_at: datetime

    # URL from which the user will retrieve their compliance results.
    download_url: str

    id: JobId

    status: ComplianceJobStatus

    type: ComplianceJobType

    # Expiration time of the upload URL.
    upload_expires_at: datetime

    # URL to which the user will upload their Tweet or user IDs.
    upload_url: str

class OptionalComplianceJob(TypedDict, total=False):
    name: ComplianceJobName

class ComplianceJob(RequiredComplianceJob, OptionalComplianceJob):
    pass
