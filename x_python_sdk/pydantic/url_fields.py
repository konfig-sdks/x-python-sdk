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

from x_python_sdk.pydantic.http_status_code import HttpStatusCode
from x_python_sdk.pydantic.media_key import MediaKey
from x_python_sdk.pydantic.url_image import UrlImage

class UrlFields(BaseModel):
    # A validly formatted URL.
    url: str = Field(alias='url')

    # Title of the page the URL points to.
    title: typing.Optional[str] = Field(None, alias='title')

    # Description of the URL landing page.
    description: typing.Optional[str] = Field(None, alias='description')

    # The URL as displayed in the Twitter client.
    display_url: typing.Optional[str] = Field(None, alias='display_url')

    # A validly formatted URL.
    expanded_url: typing.Optional[str] = Field(None, alias='expanded_url')

    images: typing.Optional[typing.List[UrlImage]] = Field(None, alias='images')

    media_key: typing.Optional[MediaKey] = Field(None, alias='media_key')

    status: typing.Optional[HttpStatusCode] = Field(None, alias='status')

    # Fully resolved url.
    unwound_url: typing.Optional[str] = Field(None, alias='unwound_url')
    class Config:
        arbitrary_types_allowed = True
