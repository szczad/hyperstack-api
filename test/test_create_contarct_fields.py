# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.create_contarct_fields import CreateContarctFields

class TestCreateContarctFields(unittest.TestCase):
    """CreateContarctFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateContarctFields:
        """Test CreateContarctFields
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateContarctFields`
        """
        model = CreateContarctFields()
        if include_optional:
            return CreateContarctFields(
                id = 56,
                org_id = 56,
                description = '',
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expiration_policy = 56,
                discount_plans = [
                    hyperstack.models.discount_plan_fields.DiscountPlanFields(
                        id = 56, 
                        resource_id = 56, 
                        resource_name = '', 
                        resource_count = 56, 
                        discount_type = '', 
                        discount_code = '', 
                        discount_percent = 1.337, 
                        discount_amount = 1.337, 
                        discount_status = '', )
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return CreateContarctFields(
        )
        """

    def testCreateContarctFields(self):
        """Test CreateContarctFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()