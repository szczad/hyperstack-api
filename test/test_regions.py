# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.regions import Regions

class TestRegions(unittest.TestCase):
    """Regions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Regions:
        """Test Regions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Regions`
        """
        model = Regions()
        if include_optional:
            return Regions(
                status = True,
                message = '',
                regions = [
                    hyperstack.models.region_fields.RegionFields(
                        id = 56, 
                        name = '', 
                        description = '', )
                    ]
            )
        else:
            return Regions(
        )
        """

    def testRegions(self):
        """Test Regions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
