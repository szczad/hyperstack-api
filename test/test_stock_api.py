# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.api.stock_api import StockApi


class TestStockApi(unittest.TestCase):
    """StockApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StockApi()

    def tearDown(self) -> None:
        pass

    def test_retrieve_gpu_stocks(self) -> None:
        """Test case for retrieve_gpu_stocks

        """
        pass


if __name__ == '__main__':
    unittest.main()
