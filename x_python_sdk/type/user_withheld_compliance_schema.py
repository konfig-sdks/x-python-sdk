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

from x_python_sdk.type.user_takedown_compliance_schema import UserTakedownComplianceSchema

class RequiredUserWithheldComplianceSchema(TypedDict):
    user_withheld: UserTakedownComplianceSchema

class OptionalUserWithheldComplianceSchema(TypedDict, total=False):
    pass

class UserWithheldComplianceSchema(RequiredUserWithheldComplianceSchema, OptionalUserWithheldComplianceSchema):
    pass
