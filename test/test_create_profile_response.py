# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.create_profile_response import CreateProfileResponse

class TestCreateProfileResponse(unittest.TestCase):
    """CreateProfileResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateProfileResponse:
        """Test CreateProfileResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateProfileResponse`
        """
        model = CreateProfileResponse()
        if include_optional:
            return CreateProfileResponse(
                status = True,
                message = '',
                profile = hyperstack.models.profile_fields.ProfileFields(
                    id = 56, 
                    name = '', 
                    description = '', 
                    data = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return CreateProfileResponse(
        )
        """

    def testCreateProfileResponse(self):
        """Test CreateProfileResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
