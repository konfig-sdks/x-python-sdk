# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.62
    Created by: https://developer.twitter.com/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from x_python_sdk import schemas  # noqa: F401


class InvalidRequestProblem(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A problem that indicates this request is invalid.
    """


    class MetaOapg:
        
        @staticmethod
        def discriminator():
            return {
                'type': {
                    'about:blank': GenericProblem,
                    'https://api.twitter.com/2/problems/client-disconnected': ClientDisconnectedProblem,
                    'https://api.twitter.com/2/problems/client-forbidden': ClientForbiddenProblem,
                    'https://api.twitter.com/2/problems/conflict': ConflictProblem,
                    'https://api.twitter.com/2/problems/disallowed-resource': DisallowedResourceProblem,
                    'https://api.twitter.com/2/problems/duplicate-rules': DuplicateRuleProblem,
                    'https://api.twitter.com/2/problems/invalid-request': InvalidRequestProblem,
                    'https://api.twitter.com/2/problems/invalid-rules': InvalidRuleProblem,
                    'https://api.twitter.com/2/problems/noncompliant-rules': NonCompliantRulesProblem,
                    'https://api.twitter.com/2/problems/not-authorized-for-field': FieldUnauthorizedProblem,
                    'https://api.twitter.com/2/problems/not-authorized-for-resource': ResourceUnauthorizedProblem,
                    'https://api.twitter.com/2/problems/oauth1-permissions': Oauth1PermissionsProblem,
                    'https://api.twitter.com/2/problems/operational-disconnect': OperationalDisconnectProblem,
                    'https://api.twitter.com/2/problems/resource-not-found': ResourceNotFoundProblem,
                    'https://api.twitter.com/2/problems/resource-unavailable': ResourceUnavailableProblem,
                    'https://api.twitter.com/2/problems/rule-cap': RulesCapProblem,
                    'https://api.twitter.com/2/problems/streaming-connection': ConnectionExceptionProblem,
                    'https://api.twitter.com/2/problems/unsupported-authentication': UnsupportedAuthenticationProblem,
                    'https://api.twitter.com/2/problems/usage-capped': UsageCapExceededProblem,
                }
            }
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    
                    
                    class errors(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            min_items = 1
                            
                            
                            class items(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    
                                    class properties:
                                        
                                        
                                        class parameters(
                                            schemas.DictSchema
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                
                                                
                                                class additional_properties(
                                                    schemas.ListSchema
                                                ):
                                                
                                                
                                                    class MetaOapg:
                                                        items = schemas.StrSchema
                                                
                                                    def __new__(
                                                        cls,
                                                        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                                    ) -> 'additional_properties':
                                                        return super().__new__(
                                                            cls,
                                                            arg,
                                                            _configuration=_configuration,
                                                        )
                                                
                                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                                        return super().__getitem__(i)
                                            
                                            def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                                                # dict_instance[name] accessor
                                                return super().__getitem__(name)
                                            
                                            def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                                                return super().get_item_oapg(name)
                                        
                                            def __new__(
                                                cls,
                                                *args: typing.Union[dict, frozendict.frozendict, ],
                                                _configuration: typing.Optional[schemas.Configuration] = None,
                                                **kwargs: typing.Union[MetaOapg.additional_properties, list, tuple, ],
                                            ) -> 'parameters':
                                                return super().__new__(
                                                    cls,
                                                    *args,
                                                    _configuration=_configuration,
                                                    **kwargs,
                                                )
                                        message = schemas.StrSchema
                                        __annotations__ = {
                                            "parameters": parameters,
                                            "message": message,
                                        }
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["parameters"]) -> MetaOapg.properties.parameters: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["parameters", "message", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["parameters"]) -> typing.Union[MetaOapg.properties.parameters, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["parameters", "message", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, ],
                                    parameters: typing.Union[MetaOapg.properties.parameters, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                                    message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'items':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        parameters=parameters,
                                        message=message,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'errors':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    __annotations__ = {
                        "errors": errors,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["errors", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> typing.Union[MetaOapg.properties.errors, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["errors", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                errors: typing.Union[MetaOapg.properties.errors, list, tuple, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    errors=errors,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                Problem,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InvalidRequestProblem':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from x_python_sdk.model.client_disconnected_problem import ClientDisconnectedProblem
from x_python_sdk.model.client_forbidden_problem import ClientForbiddenProblem
from x_python_sdk.model.conflict_problem import ConflictProblem
from x_python_sdk.model.connection_exception_problem import ConnectionExceptionProblem
from x_python_sdk.model.disallowed_resource_problem import DisallowedResourceProblem
from x_python_sdk.model.duplicate_rule_problem import DuplicateRuleProblem
from x_python_sdk.model.field_unauthorized_problem import FieldUnauthorizedProblem
from x_python_sdk.model.generic_problem import GenericProblem
from x_python_sdk.model.invalid_request_problem import InvalidRequestProblem
from x_python_sdk.model.invalid_rule_problem import InvalidRuleProblem
from x_python_sdk.model.non_compliant_rules_problem import NonCompliantRulesProblem
from x_python_sdk.model.oauth1_permissions_problem import Oauth1PermissionsProblem
from x_python_sdk.model.operational_disconnect_problem import OperationalDisconnectProblem
from x_python_sdk.model.problem import Problem
from x_python_sdk.model.resource_not_found_problem import ResourceNotFoundProblem
from x_python_sdk.model.resource_unauthorized_problem import ResourceUnauthorizedProblem
from x_python_sdk.model.resource_unavailable_problem import ResourceUnavailableProblem
from x_python_sdk.model.rules_cap_problem import RulesCapProblem
from x_python_sdk.model.unsupported_authentication_problem import UnsupportedAuthenticationProblem
from x_python_sdk.model.usage_cap_exceeded_problem import UsageCapExceededProblem
