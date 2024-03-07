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

class RequiredFilteredStreamingTweetResponseMatchingRulesItem(TypedDict):
    id: RuleId

class OptionalFilteredStreamingTweetResponseMatchingRulesItem(TypedDict, total=False):
    # A tag meant for the labeling of user provided rules.
    tag: str

class FilteredStreamingTweetResponseMatchingRulesItem(RequiredFilteredStreamingTweetResponseMatchingRulesItem, OptionalFilteredStreamingTweetResponseMatchingRulesItem):
    pass
