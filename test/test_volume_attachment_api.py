# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.api.volume_attachment_api import VolumeAttachmentApi


class TestVolumeAttachmentApi(unittest.TestCase):
    """VolumeAttachmentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VolumeAttachmentApi()

    def tearDown(self) -> None:
        pass

    def test_attach_volumes_to_virtual_machine(self) -> None:
        """Test case for attach_volumes_to_virtual_machine

        Attach volumes to virtual machine
        """
        pass

    def test_detach_volumes_from_virtual_machine(self) -> None:
        """Test case for detach_volumes_from_virtual_machine

        Detach volumes from virtual machine
        """
        pass


if __name__ == '__main__':
    unittest.main()
