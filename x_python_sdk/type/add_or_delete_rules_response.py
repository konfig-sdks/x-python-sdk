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

from x_python_sdk.type.problem import Problem
from x_python_sdk.type.rule import Rule
from x_python_sdk.type.rules_response_metadata import RulesResponseMetadata

class RequiredAddOrDeleteRulesResponse(TypedDict):
    meta: RulesResponseMetadata

class OptionalAddOrDeleteRulesResponse(TypedDict, total=False):
    # All user-specified stream filtering rules that were created.
    data: typing.List[Rule]

    errors: typing.List[Problem]

class AddOrDeleteRulesResponse(RequiredAddOrDeleteRulesResponse, OptionalAddOrDeleteRulesResponse):
    pass
