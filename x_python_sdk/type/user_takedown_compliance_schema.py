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

from x_python_sdk.type.country_code import CountryCode
from x_python_sdk.type.user_takedown_compliance_schema_user import UserTakedownComplianceSchemaUser

class RequiredUserTakedownComplianceSchema(TypedDict):
    # Event time.
    event_at: datetime

    user: UserTakedownComplianceSchemaUser

    withheld_in_countries: typing.List[CountryCode]

class OptionalUserTakedownComplianceSchema(TypedDict, total=False):
    pass

class UserTakedownComplianceSchema(RequiredUserTakedownComplianceSchema, OptionalUserTakedownComplianceSchema):
    pass
