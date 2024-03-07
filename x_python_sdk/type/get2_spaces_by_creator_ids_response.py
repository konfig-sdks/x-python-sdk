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

from x_python_sdk.type.expansions import Expansions
from x_python_sdk.type.get2_spaces_by_creator_ids_response_meta import Get2SpacesByCreatorIdsResponseMeta
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.space import Space

class RequiredGet2SpacesByCreatorIdsResponse(TypedDict):
    pass

class OptionalGet2SpacesByCreatorIdsResponse(TypedDict, total=False):
    data: typing.List[Space]

    errors: typing.List[Problem]

    includes: Expansions

    meta: Get2SpacesByCreatorIdsResponseMeta

class Get2SpacesByCreatorIdsResponse(RequiredGet2SpacesByCreatorIdsResponse, OptionalGet2SpacesByCreatorIdsResponse):
    pass
