# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.cluster_resource import ClusterResource

class TestClusterResource(unittest.TestCase):
    """ClusterResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClusterResource:
        """Test ClusterResource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClusterResource`
        """
        model = ClusterResource()
        if include_optional:
            return ClusterResource(
                id = 56,
                name = '',
                kubernetes_version = '',
                status = '',
                master_count = 56,
                node_count = 56,
                node_flavor = hyperstack.models.flavor_resource.FlavorResource(
                    id = 56, 
                    name = '', 
                    cpu = 56, 
                    ram = 1.337, 
                    disk = 56, 
                    gpu = '', 
                    gpu_count = 56, ),
                enable_public_ip = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ClusterResource(
        )
        """

    def testClusterResource(self):
        """Test ClusterResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
