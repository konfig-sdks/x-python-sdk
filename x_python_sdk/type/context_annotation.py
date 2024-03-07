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

from x_python_sdk.type.context_annotation_domain_fields import ContextAnnotationDomainFields
from x_python_sdk.type.context_annotation_entity_fields import ContextAnnotationEntityFields

class RequiredContextAnnotation(TypedDict):
    domain: ContextAnnotationDomainFields

    entity: ContextAnnotationEntityFields

class OptionalContextAnnotation(TypedDict, total=False):
    pass

class ContextAnnotation(RequiredContextAnnotation, OptionalContextAnnotation):
    pass
