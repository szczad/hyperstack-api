# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.user_default_choice_for_user_fields import UserDefaultChoiceForUserFields

class TestUserDefaultChoiceForUserFields(unittest.TestCase):
    """UserDefaultChoiceForUserFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserDefaultChoiceForUserFields:
        """Test UserDefaultChoiceForUserFields
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserDefaultChoiceForUserFields`
        """
        model = UserDefaultChoiceForUserFields()
        if include_optional:
            return UserDefaultChoiceForUserFields(
                region_id = 56,
                environment_id = 56,
                keypair_id = 56,
                flavor_id = 56,
                image_id = 56
            )
        else:
            return UserDefaultChoiceForUserFields(
        )
        """

    def testUserDefaultChoiceForUserFields(self):
        """Test UserDefaultChoiceForUserFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
