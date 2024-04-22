# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.billingmetricesfields import Billingmetricesfields

class TestBillingmetricesfields(unittest.TestCase):
    """Billingmetricesfields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Billingmetricesfields:
        """Test Billingmetricesfields
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Billingmetricesfields`
        """
        model = Billingmetricesfields()
        if include_optional:
            return Billingmetricesfields(
                resource_id = 56,
                resource_type = '',
                name = '',
                organization_id = 56,
                bill_per_minute = 1.337,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                terminate_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                total_up_time = 1.337,
                total_bill = 1.337,
                active = True,
                exclude_billing = True
            )
        else:
            return Billingmetricesfields(
        )
        """

    def testBillingmetricesfields(self):
        """Test Billingmetricesfields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
