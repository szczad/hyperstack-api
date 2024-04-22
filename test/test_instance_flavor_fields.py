# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.instance_flavor_fields import InstanceFlavorFields

class TestInstanceFlavorFields(unittest.TestCase):
    """InstanceFlavorFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstanceFlavorFields:
        """Test InstanceFlavorFields
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstanceFlavorFields`
        """
        model = InstanceFlavorFields()
        if include_optional:
            return InstanceFlavorFields(
                id = 56,
                name = '',
                cpu = 56,
                ram = 1.337,
                disk = 56,
                ephemeral = 56,
                gpu = '',
                gpu_count = 56
            )
        else:
            return InstanceFlavorFields(
        )
        """

    def testInstanceFlavorFields(self):
        """Test InstanceFlavorFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
