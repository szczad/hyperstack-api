# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.import_keypair_payload import ImportKeypairPayload

class TestImportKeypairPayload(unittest.TestCase):
    """ImportKeypairPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportKeypairPayload:
        """Test ImportKeypairPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportKeypairPayload`
        """
        model = ImportKeypairPayload()
        if include_optional:
            return ImportKeypairPayload(
                name = '',
                environment_name = '',
                public_key = ''
            )
        else:
            return ImportKeypairPayload(
                name = '',
                environment_name = '',
                public_key = '',
        )
        """

    def testImportKeypairPayload(self):
        """Test ImportKeypairPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
