# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.get_policies_response_model import GetPoliciesResponseModel

class TestGetPoliciesResponseModel(unittest.TestCase):
    """GetPoliciesResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetPoliciesResponseModel:
        """Test GetPoliciesResponseModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetPoliciesResponseModel`
        """
        model = GetPoliciesResponseModel()
        if include_optional:
            return GetPoliciesResponseModel(
                status = True,
                message = '',
                policies = [
                    hyperstack.models.policy_fields.PolicyFields(
                        id = 56, 
                        name = '', 
                        description = '', 
                        permissions = [
                            hyperstack.models.policy_permission_fields.PolicyPermissionFields(
                                id = 56, 
                                resource = '', 
                                permission = '', )
                            ], 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return GetPoliciesResponseModel(
        )
        """

    def testGetPoliciesResponseModel(self):
        """Test GetPoliciesResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()