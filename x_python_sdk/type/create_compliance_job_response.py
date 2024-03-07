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
from x_python_sdk.type.problem import Problem

class RequiredCreateComplianceJobResponse(TypedDict):
    pass

class OptionalCreateComplianceJobResponse(TypedDict, total=False):
    data: ComplianceJob

    errors: typing.List[Problem]

class CreateComplianceJobResponse(RequiredCreateComplianceJobResponse, OptionalCreateComplianceJobResponse):
    pass
