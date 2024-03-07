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

from x_python_sdk.type.animated_gif import AnimatedGif
from x_python_sdk.type.media import Media
from x_python_sdk.type.photo import Photo
from x_python_sdk.type.video import Video

Photo = typing.Union[Media,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
