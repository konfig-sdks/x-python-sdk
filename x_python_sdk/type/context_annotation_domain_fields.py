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


class RequiredContextAnnotationDomainFields(TypedDict):
    # The unique id for a context annotation domain.
    id: str

class OptionalContextAnnotationDomainFields(TypedDict, total=False):
    # Description of the context annotation domain.
    description: str

    # Name of the context annotation domain.
    name: str

class ContextAnnotationDomainFields(RequiredContextAnnotationDomainFields, OptionalContextAnnotationDomainFields):
    pass
