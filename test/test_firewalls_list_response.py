# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.firewalls_list_response import FirewallsListResponse

class TestFirewallsListResponse(unittest.TestCase):
    """FirewallsListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FirewallsListResponse:
        """Test FirewallsListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FirewallsListResponse`
        """
        model = FirewallsListResponse()
        if include_optional:
            return FirewallsListResponse(
                status = True,
                message = '',
                firewalls = [
                    hyperstack.models.firewall_detail_fields.FirewallDetailFields(
                        id = 56, 
                        name = '', 
                        description = '', 
                        environment = hyperstack.models.firewall_environment_fields.FirewallEnvironmentFields(
                            id = 56, 
                            name = '', 
                            region = '', ), 
                        status = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        rules = [
                            hyperstack.models.security_group_rule_fields.SecurityGroupRuleFields(
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
                        attachments = [
                            hyperstack.models.firewall_attachment_model.FirewallAttachmentModel(
                                id = 56, 
                                status = '', 
                                vm = hyperstack.models.firewall_attachment_vm_model.FirewallAttachmentVMModel(
                                    id = 56, 
                                    name = '', 
                                    flavor = '', 
                                    status = '', 
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], )
                    ]
            )
        else:
            return FirewallsListResponse(
        )
        """

    def testFirewallsListResponse(self):
        """Test FirewallsListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()