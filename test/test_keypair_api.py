# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.api.keypair_api import KeypairApi


class TestKeypairApi(unittest.TestCase):
    """KeypairApi unit test stubs"""

    def setUp(self) -> None:
        self.api = KeypairApi()

    def tearDown(self) -> None:
        pass

    def test_delete_key_pair(self) -> None:
        """Test case for delete_key_pair

        Delete key pair
        """
        pass

    def test_import_key_pair(self) -> None:
        """Test case for import_key_pair

        Import key pair
        """
        pass

    def test_list_key_pairs(self) -> None:
        """Test case for list_key_pairs

        List key pairs
        """
        pass

    def test_update_key_pair_name(self) -> None:
        """Test case for update_key_pair_name

        Update key pair name
        """
        pass


if __name__ == '__main__':
    unittest.main()
