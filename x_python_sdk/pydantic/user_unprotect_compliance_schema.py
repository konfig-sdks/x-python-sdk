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

from x_python_sdk.pydantic.user_compliance_schema import UserComplianceSchema

class UserUnprotectComplianceSchema(BaseModel):
    user_unprotect: UserComplianceSchema = Field(alias='user_unprotect')
    class Config:
        arbitrary_types_allowed = True
