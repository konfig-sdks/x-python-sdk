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

from x_python_sdk.pydantic.tweet_id import TweetId
from x_python_sdk.pydantic.user_entities import UserEntities
from x_python_sdk.pydantic.user_id import UserId
from x_python_sdk.pydantic.user_name import UserName
from x_python_sdk.pydantic.user_public_metrics import UserPublicMetrics
from x_python_sdk.pydantic.user_withheld import UserWithheld

class User(BaseModel):
    id: UserId = Field(alias='id')

    # The friendly name of this User, as shown on their profile.
    name: str = Field(alias='name')

    username: UserName = Field(alias='username')

    # The text of this User's profile description (also known as bio), if the User provided one.
    description: typing.Optional[str] = Field(None, alias='description')

    # Creation time of this User.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    entities: typing.Optional[UserEntities] = Field(None, alias='entities')

    # The location specified in the User's profile, if the User provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.
    location: typing.Optional[str] = Field(None, alias='location')

    pinned_tweet_id: typing.Optional[TweetId] = Field(None, alias='pinned_tweet_id')

    # The URL to the profile image for this User.
    profile_image_url: typing.Optional[str] = Field(None, alias='profile_image_url')

    # Indicates if this User has chosen to protect their Tweets (in other words, if this User's Tweets are private).
    protected: typing.Optional[bool] = Field(None, alias='protected')

    public_metrics: typing.Optional[UserPublicMetrics] = Field(None, alias='public_metrics')

    # The URL specified in the User's profile.
    url: typing.Optional[str] = Field(None, alias='url')

    # Indicate if this User is a verified Twitter User.
    verified: typing.Optional[bool] = Field(None, alias='verified')

    # The Twitter Blue verified type of the user, eg: blue, government, business or none.
    verified_type: typing.Optional[str] = Field(None, alias='verified_type')

    withheld: typing.Optional[UserWithheld] = Field(None, alias='withheld')
    class Config:
        arbitrary_types_allowed = True
