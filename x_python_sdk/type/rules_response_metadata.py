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

from x_python_sdk.type.next_token import NextToken
from x_python_sdk.type.rules_request_summary import RulesRequestSummary

class RequiredRulesResponseMetadata(TypedDict):
    sent: str

class OptionalRulesResponseMetadata(TypedDict, total=False):
    summary: RulesRequestSummary

    next_token: NextToken

    # Number of Rules in result set.
    result_count: int

class RulesResponseMetadata(RequiredRulesResponseMetadata, OptionalRulesResponseMetadata):
    pass
