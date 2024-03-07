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
from x_python_sdk.type.user_entities import UserEntities
from x_python_sdk.type.user_id import UserId
from x_python_sdk.type.user_name import UserName
from x_python_sdk.type.user_public_metrics import UserPublicMetrics
from x_python_sdk.type.user_withheld import UserWithheld

class RequiredUser(TypedDict):
    id: UserId

    # The friendly name of this User, as shown on their profile.
    name: str

    username: UserName

class OptionalUser(TypedDict, total=False):
    # The text of this User's profile description (also known as bio), if the User provided one.
    description: str

    # Creation time of this User.
    created_at: datetime

    entities: UserEntities

    # The location specified in the User's profile, if the User provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.
    location: str

    pinned_tweet_id: TweetId

    # The URL to the profile image for this User.
    profile_image_url: str

    # Indicates if this User has chosen to protect their Tweets (in other words, if this User's Tweets are private).
    protected: bool

    public_metrics: UserPublicMetrics

    # The URL specified in the User's profile.
    url: str

    # Indicate if this User is a verified Twitter User.
    verified: bool

    # The Twitter Blue verified type of the user, eg: blue, government, business or none.
    verified_type: str

    withheld: UserWithheld

class User(RequiredUser, OptionalUser):
    pass
