# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.new_configurations_response import NewConfigurationsResponse

class TestNewConfigurationsResponse(unittest.TestCase):
    """NewConfigurationsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewConfigurationsResponse:
        """Test NewConfigurationsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewConfigurationsResponse`
        """
        model = NewConfigurationsResponse()
        if include_optional:
            return NewConfigurationsResponse(
                var_1x = 56,
                var_2x = 56,
                var_4x = 56,
                var_8x = 56,
                var_10x = 56
            )
        else:
            return NewConfigurationsResponse(
        )
        """

    def testNewConfigurationsResponse(self):
        """Test NewConfigurationsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
