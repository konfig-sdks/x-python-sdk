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

from x_python_sdk.type.client_disconnected_problem import ClientDisconnectedProblem
from x_python_sdk.type.client_forbidden_problem import ClientForbiddenProblem
from x_python_sdk.type.conflict_problem import ConflictProblem
from x_python_sdk.type.connection_exception_problem import ConnectionExceptionProblem
from x_python_sdk.type.disallowed_resource_problem import DisallowedResourceProblem
from x_python_sdk.type.duplicate_rule_problem import DuplicateRuleProblem
from x_python_sdk.type.field_unauthorized_problem import FieldUnauthorizedProblem
from x_python_sdk.type.generic_problem import GenericProblem
from x_python_sdk.type.invalid_request_problem import InvalidRequestProblem
from x_python_sdk.type.invalid_rule_problem import InvalidRuleProblem
from x_python_sdk.type.non_compliant_rules_problem import NonCompliantRulesProblem
from x_python_sdk.type.oauth1_permissions_problem import Oauth1PermissionsProblem
from x_python_sdk.type.operational_disconnect_problem import OperationalDisconnectProblem
from x_python_sdk.type.problem import Problem
from x_python_sdk.type.resource_not_found_problem import ResourceNotFoundProblem
from x_python_sdk.type.resource_unauthorized_problem import ResourceUnauthorizedProblem
from x_python_sdk.type.resource_unavailable_problem import ResourceUnavailableProblem
from x_python_sdk.type.rules_cap_problem import RulesCapProblem
from x_python_sdk.type.unsupported_authentication_problem import UnsupportedAuthenticationProblem
from x_python_sdk.type.usage_cap_exceeded_problem import UsageCapExceededProblem

DisallowedResourceProblem = typing.Union[Problem,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
