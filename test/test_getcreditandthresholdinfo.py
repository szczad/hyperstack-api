# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.getcreditandthresholdinfo import Getcreditandthresholdinfo

class TestGetcreditandthresholdinfo(unittest.TestCase):
    """Getcreditandthresholdinfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Getcreditandthresholdinfo:
        """Test Getcreditandthresholdinfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Getcreditandthresholdinfo`
        """
        model = Getcreditandthresholdinfo()
        if include_optional:
            return Getcreditandthresholdinfo(
                credit = 1.337,
                threshold = 1.337,
                can_create_instance = True
            )
        else:
            return Getcreditandthresholdinfo(
        )
        """

    def testGetcreditandthresholdinfo(self):
        """Test Getcreditandthresholdinfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()