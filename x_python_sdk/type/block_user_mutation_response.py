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

from x_python_sdk.type.block_user_mutation_response_data import BlockUserMutationResponseData
from x_python_sdk.type.problem import Problem

class RequiredBlockUserMutationResponse(TypedDict):
    pass

class OptionalBlockUserMutationResponse(TypedDict, total=False):
    data: BlockUserMutationResponseData

    errors: typing.List[Problem]

class BlockUserMutationResponse(RequiredBlockUserMutationResponse, OptionalBlockUserMutationResponse):
    pass
