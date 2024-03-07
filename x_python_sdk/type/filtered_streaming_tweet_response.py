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

from x_python_sdk.type.expansions import Expansions
from x_python_sdk.type.filtered_streaming_tweet_response_matching_rules import FilteredStreamingTweetResponseMatchingRules
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.tweet import Tweet

class RequiredFilteredStreamingTweetResponse(TypedDict):
    pass

class OptionalFilteredStreamingTweetResponse(TypedDict, total=False):
    data: Tweet

    errors: typing.List[Problem]

    includes: Expansions

    matching_rules: FilteredStreamingTweetResponseMatchingRules

class FilteredStreamingTweetResponse(RequiredFilteredStreamingTweetResponse, OptionalFilteredStreamingTweetResponse):
    pass
