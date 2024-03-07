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

from x_python_sdk.type.compliance_job import ComplianceJob
from x_python_sdk.type.get2_compliance_jobs_response_meta import Get2ComplianceJobsResponseMeta
from x_python_sdk.type.problem import Problem

class RequiredGet2ComplianceJobsResponse(TypedDict):
    pass

class OptionalGet2ComplianceJobsResponse(TypedDict, total=False):
    data: typing.List[ComplianceJob]

    errors: typing.List[Problem]

    meta: Get2ComplianceJobsResponseMeta

class Get2ComplianceJobsResponse(RequiredGet2ComplianceJobsResponse, OptionalGet2ComplianceJobsResponse):
    pass
