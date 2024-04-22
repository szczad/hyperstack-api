# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.instance import Instance

class TestInstance(unittest.TestCase):
    """Instance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Instance:
        """Test Instance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Instance`
        """
        model = Instance()
        if include_optional:
            return Instance(
                status = True,
                message = '',
                instance = hyperstack.models.instance_fields.InstanceFields(
                    id = 56, 
                    name = '', 
                    status = '', 
                    environment = hyperstack.models.instance_environment_fields.InstanceEnvironmentFields(
                        id = 56, 
                        name = '', 
                        org_id = 56, 
                        region = '', ), 
                    image = hyperstack.models.instance_image_fields.InstanceImageFields(
                        name = '', ), 
                    flavor = hyperstack.models.instance_flavor_fields.InstanceFlavorFields(
                        id = 56, 
                        name = '', 
                        cpu = 56, 
                        ram = 1.337, 
                        disk = 56, 
                        ephemeral = 56, 
                        gpu = '', 
                        gpu_count = 56, ), 
                    os = '', 
                    keypair = hyperstack.models.instance_keypair_fields.InstanceKeypairFields(
                        name = '', ), 
                    volume_attachments = [
                        hyperstack.models.volume_attachment_fields.VolumeAttachmentFields(
                            volume = hyperstack.models.volume_fieldsfor_instance.VolumeFieldsforInstance(
                                id = 56, 
                                name = '', 
                                description = '', 
                                volume_type = '', 
                                size = 56, ), 
                            status = '', 
                            device = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    security_rules = [
                        hyperstack.models.security_rules_fieldsfor_instance.SecurityRulesFieldsforInstance(
                            id = 56, 
                            direction = '', 
                            protocol = '', 
                            port_range_min = 56, 
                            port_range_max = 56, 
                            ethertype = '', 
                            remote_ip_prefix = '', 
                            status = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    power_state = '', 
                    vm_state = '', 
                    fixed_ip = '', 
                    floating_ip = '', 
                    floating_ip_status = '', 
                    locked = True, 
                    contract_id = 56, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    labels = [
                        ''
                        ], )
            )
        else:
            return Instance(
        )
        """

    def testInstance(self):
        """Test Instance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
