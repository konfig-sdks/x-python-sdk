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

from x_python_sdk.pydantic.rule_id import RuleId

class Rule(BaseModel):
    # The filterlang value of the rule.
    value: str = Field(alias='value')

    id: typing.Optional[RuleId] = Field(None, alias='id')

    # A tag meant for the labeling of user provided rules.
    tag: typing.Optional[str] = Field(None, alias='tag')
    class Config:
        arbitrary_types_allowed = True
