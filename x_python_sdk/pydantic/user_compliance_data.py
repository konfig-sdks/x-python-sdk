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

from x_python_sdk.pydantic.user_delete_compliance_schema import UserDeleteComplianceSchema
from x_python_sdk.pydantic.user_profile_modification_compliance_schema import UserProfileModificationComplianceSchema
from x_python_sdk.pydantic.user_protect_compliance_schema import UserProtectComplianceSchema
from x_python_sdk.pydantic.user_scrub_geo_schema import UserScrubGeoSchema
from x_python_sdk.pydantic.user_suspend_compliance_schema import UserSuspendComplianceSchema
from x_python_sdk.pydantic.user_undelete_compliance_schema import UserUndeleteComplianceSchema
from x_python_sdk.pydantic.user_unprotect_compliance_schema import UserUnprotectComplianceSchema
from x_python_sdk.pydantic.user_unsuspend_compliance_schema import UserUnsuspendComplianceSchema
from x_python_sdk.pydantic.user_withheld_compliance_schema import UserWithheldComplianceSchema

UserComplianceData = typing.Union[UserProtectComplianceSchema,UserUnprotectComplianceSchema,UserDeleteComplianceSchema,UserUndeleteComplianceSchema,UserSuspendComplianceSchema,UserUnsuspendComplianceSchema,UserWithheldComplianceSchema,UserScrubGeoSchema,UserProfileModificationComplianceSchema]
