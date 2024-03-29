# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.node_stock_payload_model import NodeStockPayloadModel

class TestNodeStockPayloadModel(unittest.TestCase):
    """NodeStockPayloadModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NodeStockPayloadModel:
        """Test NodeStockPayloadModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NodeStockPayloadModel`
        """
        model = NodeStockPayloadModel()
        if include_optional:
            return NodeStockPayloadModel(
                stocks = [
                    hyperstack.models.node_payload_model.NodePayloadModel(
                        region = '', 
                        nodes = [
                            hyperstack.models.node_power_usage_model.NodePowerUsageModel(
                                openstack_id = '', 
                                openstack_name = '', 
                                nexgen_name = '', 
                                status = '', 
                                provision_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                sunset_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                stocks = [
                                    hyperstack.models.node_stocks_payload.NodeStocksPayload(
                                        name = '', 
                                        type = '', 
                                        total = 56, 
                                        in_use = 56, )
                                    ], 
                                power_usages = hyperstack.models.power_usage_model.PowerUsageModel(
                                    value = 1.337, 
                                    unit = '', ), )
                            ], )
                    ]
            )
        else:
            return NodeStockPayloadModel(
        )
        """

    def testNodeStockPayloadModel(self):
        """Test NodeStockPayloadModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
