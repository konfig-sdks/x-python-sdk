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

from x_python_sdk.type.http_status_code import HttpStatusCode
from x_python_sdk.type.media_key import MediaKey
from x_python_sdk.type.url_image import UrlImage

class RequiredUrlFields(TypedDict):
    # A validly formatted URL.
    url: str

class OptionalUrlFields(TypedDict, total=False):
    # Title of the page the URL points to.
    title: str

    # Description of the URL landing page.
    description: str

    # The URL as displayed in the Twitter client.
    display_url: str

    # A validly formatted URL.
    expanded_url: str

    images: typing.List[UrlImage]

    media_key: MediaKey

    status: HttpStatusCode

    # Fully resolved url.
    unwound_url: str

class UrlFields(RequiredUrlFields, OptionalUrlFields):
    pass
