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

from x_python_sdk.pydantic.compliance_job import ComplianceJob
from x_python_sdk.pydantic.get2_compliance_jobs_response_meta import Get2ComplianceJobsResponseMeta
from x_python_sdk.pydantic.problem import Problem

class Get2ComplianceJobsResponse(BaseModel):
    data: typing.Optional[typing.List[ComplianceJob]] = Field(None, alias='data')

    errors: typing.Optional[typing.List[Problem]] = Field(None, alias='errors')

    meta: typing.Optional[Get2ComplianceJobsResponseMeta] = Field(None, alias='meta')
    class Config:
        arbitrary_types_allowed = True
