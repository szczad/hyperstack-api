# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.api_key_verify_response import ApiKeyVerifyResponse

class TestApiKeyVerifyResponse(unittest.TestCase):
    """ApiKeyVerifyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiKeyVerifyResponse:
        """Test ApiKeyVerifyResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiKeyVerifyResponse`
        """
        model = ApiKeyVerifyResponse()
        if include_optional:
            return ApiKeyVerifyResponse(
                status = True,
                message = '',
                api_key = hyperstack.models.api_key_verify_fields.ApiKeyVerifyFields(
                    user_id = 56, 
                    org_id = 56, 
                    user_role = '', 
                    sub = '', )
            )
        else:
            return ApiKeyVerifyResponse(
        )
        """

    def testApiKeyVerifyResponse(self):
        """Test ApiKeyVerifyResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()