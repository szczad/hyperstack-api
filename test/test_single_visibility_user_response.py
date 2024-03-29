# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.single_visibility_user_response import SingleVisibilityUserResponse

class TestSingleVisibilityUserResponse(unittest.TestCase):
    """SingleVisibilityUserResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SingleVisibilityUserResponse:
        """Test SingleVisibilityUserResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleVisibilityUserResponse`
        """
        model = SingleVisibilityUserResponse()
        if include_optional:
            return SingleVisibilityUserResponse(
                id = 56,
                user_id = 56,
                stock_visible = True
            )
        else:
            return SingleVisibilityUserResponse(
                id = 56,
                user_id = 56,
                stock_visible = True,
        )
        """

    def testSingleVisibilityUserResponse(self):
        """Test SingleVisibilityUserResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
