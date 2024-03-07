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

from x_python_sdk.type.tweet_id import TweetId
from x_python_sdk.type.user_scrub_geo_object_schema_user import UserScrubGeoObjectSchemaUser

class RequiredUserScrubGeoObjectSchema(TypedDict):
    # Event time.
    event_at: datetime

    up_to_tweet_id: TweetId

    user: UserScrubGeoObjectSchemaUser

class OptionalUserScrubGeoObjectSchema(TypedDict, total=False):
    pass

class UserScrubGeoObjectSchema(RequiredUserScrubGeoObjectSchema, OptionalUserScrubGeoObjectSchema):
    pass
