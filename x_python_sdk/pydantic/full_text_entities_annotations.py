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

from x_python_sdk.pydantic.entity_indices_inclusive_inclusive import EntityIndicesInclusiveInclusive

FullTextEntitiesAnnotations = typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
