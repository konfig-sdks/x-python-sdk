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

from x_python_sdk.pydantic.country_code import CountryCode
from x_python_sdk.pydantic.user_takedown_compliance_schema_user import UserTakedownComplianceSchemaUser

class UserTakedownComplianceSchema(BaseModel):
    # Event time.
    event_at: datetime = Field(alias='event_at')

    user: UserTakedownComplianceSchemaUser = Field(alias='user')

    withheld_in_countries: typing.List[CountryCode] = Field(alias='withheld_in_countries')
    class Config:
        arbitrary_types_allowed = True
