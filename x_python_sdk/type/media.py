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
from x_python_sdk.type.media_height import MediaHeight
from x_python_sdk.type.media_key import MediaKey
from x_python_sdk.type.media_width import MediaWidth
from x_python_sdk.type.photo import Photo
from x_python_sdk.type.video import Video

class RequiredMedia(TypedDict):
    type: str

class OptionalMedia(TypedDict, total=False):
    height: MediaHeight

    media_key: MediaKey

    width: MediaWidth

class Media(RequiredMedia, OptionalMedia):
    pass
