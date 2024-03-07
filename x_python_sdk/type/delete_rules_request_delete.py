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

class RequiredDeleteRulesRequestDelete(TypedDict):
    pass

class OptionalDeleteRulesRequestDelete(TypedDict, total=False):
    # IDs of all deleted user-specified stream filtering rules.
    ids: typing.List[RuleId]

    # Values of all deleted user-specified stream filtering rules.
    values: typing.List[str]

class DeleteRulesRequestDelete(RequiredDeleteRulesRequestDelete, OptionalDeleteRulesRequestDelete):
    pass
