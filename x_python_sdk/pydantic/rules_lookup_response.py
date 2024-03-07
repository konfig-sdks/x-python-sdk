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

from x_python_sdk.pydantic.rule import Rule
from x_python_sdk.pydantic.rules_response_metadata import RulesResponseMetadata

class RulesLookupResponse(BaseModel):
    meta: RulesResponseMetadata = Field(alias='meta')

    data: typing.Optional[typing.List[Rule]] = Field(None, alias='data')
    class Config:
        arbitrary_types_allowed = True
