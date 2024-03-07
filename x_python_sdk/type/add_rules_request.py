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

from x_python_sdk.type.rule_no_id import RuleNoId

class RequiredAddRulesRequest(TypedDict):
    add: typing.List[RuleNoId]

class OptionalAddRulesRequest(TypedDict, total=False):
    pass

class AddRulesRequest(RequiredAddRulesRequest, OptionalAddRulesRequest):
    pass
