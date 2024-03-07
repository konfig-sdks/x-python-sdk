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

from x_python_sdk.type.tweet_delete_compliance_schema import TweetDeleteComplianceSchema
from x_python_sdk.type.tweet_drop_compliance_schema import TweetDropComplianceSchema
from x_python_sdk.type.tweet_edit_compliance_schema import TweetEditComplianceSchema
from x_python_sdk.type.tweet_undrop_compliance_schema import TweetUndropComplianceSchema
from x_python_sdk.type.tweet_withheld_compliance_schema import TweetWithheldComplianceSchema

TweetComplianceData = typing.Union[TweetDeleteComplianceSchema,TweetWithheldComplianceSchema,TweetDropComplianceSchema,TweetUndropComplianceSchema,TweetEditComplianceSchema]
