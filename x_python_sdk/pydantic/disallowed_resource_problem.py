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

from x_python_sdk.pydantic.client_disconnected_problem import ClientDisconnectedProblem
from x_python_sdk.pydantic.client_forbidden_problem import ClientForbiddenProblem
from x_python_sdk.pydantic.conflict_problem import ConflictProblem
from x_python_sdk.pydantic.connection_exception_problem import ConnectionExceptionProblem
from x_python_sdk.pydantic.disallowed_resource_problem import DisallowedResourceProblem
from x_python_sdk.pydantic.duplicate_rule_problem import DuplicateRuleProblem
from x_python_sdk.pydantic.field_unauthorized_problem import FieldUnauthorizedProblem
from x_python_sdk.pydantic.generic_problem import GenericProblem
from x_python_sdk.pydantic.invalid_request_problem import InvalidRequestProblem
from x_python_sdk.pydantic.invalid_rule_problem import InvalidRuleProblem
from x_python_sdk.pydantic.non_compliant_rules_problem import NonCompliantRulesProblem
from x_python_sdk.pydantic.oauth1_permissions_problem import Oauth1PermissionsProblem
from x_python_sdk.pydantic.operational_disconnect_problem import OperationalDisconnectProblem
from x_python_sdk.pydantic.problem import Problem
from x_python_sdk.pydantic.resource_not_found_problem import ResourceNotFoundProblem
from x_python_sdk.pydantic.resource_unauthorized_problem import ResourceUnauthorizedProblem
from x_python_sdk.pydantic.resource_unavailable_problem import ResourceUnavailableProblem
from x_python_sdk.pydantic.rules_cap_problem import RulesCapProblem
from x_python_sdk.pydantic.unsupported_authentication_problem import UnsupportedAuthenticationProblem
from x_python_sdk.pydantic.usage_cap_exceeded_problem import UsageCapExceededProblem

DisallowedResourceProblem = typing.Union[Problem,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
