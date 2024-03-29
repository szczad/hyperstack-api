# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.discount_detail_response import DiscountDetailResponse

class TestDiscountDetailResponse(unittest.TestCase):
    """DiscountDetailResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiscountDetailResponse:
        """Test DiscountDetailResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscountDetailResponse`
        """
        model = DiscountDetailResponse()
        if include_optional:
            return DiscountDetailResponse(
                status = True,
                message = '',
                discount_plan = [
                    hyperstack.models.insert_discount_plan_fields.InsertDiscountPlanFields(
                        org_id = 56, 
                        org_name = '', 
                        discount_resources = [
                            hyperstack.models.discount_resource_fields.DiscountResourceFields(
                                resource_id = 56, 
                                discount_percent = 1.337, )
                            ], 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        discount_status = '', )
                    ]
            )
        else:
            return DiscountDetailResponse(
        )
        """

    def testDiscountDetailResponse(self):
        """Test DiscountDetailResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
