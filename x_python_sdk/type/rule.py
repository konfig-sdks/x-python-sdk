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

from x_python_sdk.type.rule_id import RuleId

class RequiredRule(TypedDict):
    # The filterlang value of the rule.
    value: str

class OptionalRule(TypedDict, total=False):
    id: RuleId

    # A tag meant for the labeling of user provided rules.
    tag: str

class Rule(RequiredRule, OptionalRule):
    pass
