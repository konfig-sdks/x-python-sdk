# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.62
    Created by: https://developer.twitter.com/
"""

from x_python_sdk.paths._2_openapi_json.get import GetOpenApiSpec
from x_python_sdk.apis.tags.general_api_raw import GeneralApiRaw


class GeneralApi(
    GetOpenApiSpec,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: GeneralApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = GeneralApiRaw(api_client)