# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.api.callbacks_api import CallbacksApi


class TestCallbacksApi(unittest.TestCase):
    """CallbacksApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CallbacksApi()

    def tearDown(self) -> None:
        pass

    def test_attach_a_callback_to_a_volume(self) -> None:
        """Test case for attach_a_callback_to_a_volume

        Attach a callback to a volume
        """
        pass

    def test_attach_a_callback_to_an_instance(self) -> None:
        """Test case for attach_a_callback_to_an_instance

        Attach a callback to an instance
        """
        pass

    def test_delete_a_callback_url_for_an_instance(self) -> None:
        """Test case for delete_a_callback_url_for_an_instance

        Delete a callback URL for an instance
        """
        pass

    def test_delete_callback_url_for_a_volume(self) -> None:
        """Test case for delete_callback_url_for_a_volume

        Delete callback URL for a volume
        """
        pass

    def test_update_a_callback_url(self) -> None:
        """Test case for update_a_callback_url

        Update a callback URL
        """
        pass

    def test_update_callback_url_for_volume(self) -> None:
        """Test case for update_callback_url_for_volume

        Update callback URL for volume
        """
        pass


if __name__ == '__main__':
    unittest.main()
