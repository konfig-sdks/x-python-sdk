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


class RequiredEntityIndicesInclusiveInclusive(TypedDict):
    # Index (zero-based) at which position this entity ends.  The index is inclusive.
    end: int

    # Index (zero-based) at which position this entity starts.  The index is inclusive.
    start: int

class OptionalEntityIndicesInclusiveInclusive(TypedDict, total=False):
    pass

class EntityIndicesInclusiveInclusive(RequiredEntityIndicesInclusiveInclusive, OptionalEntityIndicesInclusiveInclusive):
    pass
