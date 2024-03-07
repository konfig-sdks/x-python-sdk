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

from x_python_sdk.type.user_compliance_schema_user import UserComplianceSchemaUser

class RequiredUserComplianceSchema(TypedDict):
    # Event time.
    event_at: datetime

    user: UserComplianceSchemaUser

class OptionalUserComplianceSchema(TypedDict, total=False):
    pass

class UserComplianceSchema(RequiredUserComplianceSchema, OptionalUserComplianceSchema):
    pass
