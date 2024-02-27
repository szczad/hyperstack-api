# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.create_update_compliance_response import CreateUpdateComplianceResponse

class TestCreateUpdateComplianceResponse(unittest.TestCase):
    """CreateUpdateComplianceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateUpdateComplianceResponse:
        """Test CreateUpdateComplianceResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateUpdateComplianceResponse`
        """
        model = CreateUpdateComplianceResponse()
        if include_optional:
            return CreateUpdateComplianceResponse(
                status = True,
                message = '',
                compliance = hyperstack.models.compliance_model_fields.ComplianceModelFields(
                    id = 56, 
                    gpu_model = '', 
                    resource_type = '', 
                    base_value = 56, 
                    variation_min = 56, 
                    variation_max = 56, 
                    variation_unit = 56, )
            )
        else:
            return CreateUpdateComplianceResponse(
        )
        """

    def testCreateUpdateComplianceResponse(self):
        """Test CreateUpdateComplianceResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()