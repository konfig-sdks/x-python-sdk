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

class RequiredCreateComplianceJobRequest(TypedDict):
    # Type of compliance job to list.
    type: str

class OptionalCreateComplianceJobRequest(TypedDict, total=False):
    name: ComplianceJobName

    # If true, this endpoint will return a pre-signed URL with resumable uploads enabled.
    resumable: bool

class CreateComplianceJobRequest(RequiredCreateComplianceJobRequest, OptionalCreateComplianceJobRequest):
    pass
