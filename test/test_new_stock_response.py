# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.new_stock_response import NewStockResponse

class TestNewStockResponse(unittest.TestCase):
    """NewStockResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NewStockResponse:
        """Test NewStockResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewStockResponse`
        """
        model = NewStockResponse()
        if include_optional:
            return NewStockResponse(
                region = '',
                stock_type = '',
                models = [
                    hyperstack.models.new_model_response.NewModelResponse(
                        model = '', 
                        available = '', 
                        planned_7_days = '', 
                        planned_30_days = '', 
                        planned_100_days = '', 
                        configurations = hyperstack.models.new_configurations_response.NewConfigurationsResponse(
                            1x = 56, 
                            2x = 56, 
                            4x = 56, 
                            8x = 56, 
                            10x = 56, ), )
                    ]
            )
        else:
            return NewStockResponse(
        )
        """

    def testNewStockResponse(self):
        """Test NewStockResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
