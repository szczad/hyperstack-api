# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.node_response_model import NodeResponseModel

class TestNodeResponseModel(unittest.TestCase):
    """NodeResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NodeResponseModel:
        """Test NodeResponseModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NodeResponseModel`
        """
        model = NodeResponseModel()
        if include_optional:
            return NodeResponseModel(
                region = '',
                nodes = [
                    hyperstack.models.node_model.NodeModel(
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
                            ], )
                    ]
            )
        else:
            return NodeResponseModel(
        )
        """

    def testNodeResponseModel(self):
        """Test NodeResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
