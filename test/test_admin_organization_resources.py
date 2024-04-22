# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.admin_organization_resources import AdminOrganizationResources

class TestAdminOrganizationResources(unittest.TestCase):
    """AdminOrganizationResources unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdminOrganizationResources:
        """Test AdminOrganizationResources
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdminOrganizationResources`
        """
        model = AdminOrganizationResources()
        if include_optional:
            return AdminOrganizationResources(
                organization_id = 56,
                environments = [
                    hyperstack.models.admin_envrionment_resources.AdminEnvrionmentResources(
                        id = 56, 
                        name = '', 
                        region = '', 
                        instances = [
                            hyperstack.models.admin_instance_resources.AdminInstanceResources(
                                id = 56, 
                                name = '', 
                                openstack_id = '', 
                                host = '', 
                                status = '', 
                                flavor = hyperstack.models.admin_flavor_resource.AdminFlavorResource(
                                    id = 56, 
                                    openstack_id = '', 
                                    name = '', 
                                    region_name = '', 
                                    cpu = 56, 
                                    ram = 1.337, 
                                    disk = 56, 
                                    gpu = '', 
                                    status = '', 
                                    gpu_count = 56, 
                                    stock_available = True, 
                                    nodes = [
                                        hyperstack.models.admin_node_resource.AdminNodeResource(
                                            id = 56, 
                                            openstack_id = '', 
                                            name = '', 
                                            available = 56, 
                                            status = '', 
                                            provision_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            organizations = [
                                                56
                                                ], )
                                        ], 
                                    vms = [
                                        56
                                        ], 
                                    is_public = True, 
                                    is_custom = True, 
                                    ephemeral = 56, 
                                    description = '', 
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                image_id = 56, 
                                volume_id = 56, 
                                keypair_name = '', 
                                fixed_ip = '', 
                                floating_ip = '', 
                                contract_id = 56, 
                                floating_ip_status = '', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        volumes = [
                            hyperstack.models.admin_volume_resource.AdminVolumeResource(
                                id = 56, 
                                name = '', 
                                openstack_id = '', 
                                type = '', 
                                size = 56, 
                                status = '', 
                                bootable = True, 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        containers = [
                            hyperstack.models.admin_container_resource.AdminContainerResource(
                                id = 56, 
                                name = '', 
                                status = '', 
                                image = '', 
                                fixed_ip = '', 
                                floating_ip = '', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        clusters = [
                            hyperstack.models.admin_cluster_resource.AdminClusterResource(
                                id = 56, 
                                name = '', 
                                kubernetes_version = '', 
                                status = '', 
                                master_count = 56, 
                                node_count = 56, 
                                node_flavor = hyperstack.models.admin_flavor_resource.AdminFlavorResource(
                                    id = 56, 
                                    openstack_id = '', 
                                    name = '', 
                                    region_name = '', 
                                    cpu = 56, 
                                    ram = 1.337, 
                                    disk = 56, 
                                    gpu = '', 
                                    status = '', 
                                    gpu_count = 56, 
                                    stock_available = True, 
                                    is_public = True, 
                                    is_custom = True, 
                                    ephemeral = 56, 
                                    description = '', 
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                enable_public_ip = True, 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return AdminOrganizationResources(
        )
        """

    def testAdminOrganizationResources(self):
        """Test AdminOrganizationResources"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()