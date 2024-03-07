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

class CreateComplianceJobRequest(BaseModel):
    # Type of compliance job to list.
    type: Literal["tweets", "users"] = Field(alias='type')

    name: typing.Optional[ComplianceJobName] = Field(None, alias='name')

    # If true, this endpoint will return a pre-signed URL with resumable uploads enabled.
    resumable: typing.Optional[bool] = Field(None, alias='resumable')
    class Config:
        arbitrary_types_allowed = True
