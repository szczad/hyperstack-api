# coding: utf-8

# flake8: noqa

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.1.0"

# import apis into sdk package
from hyperstack.api.customer_contract_api import CustomerContractApi
from hyperstack.api.pricebook_api import PricebookApi
from hyperstack.api.alive_api import AliveApi
from hyperstack.api.api_key_api import ApiKeyApi
from hyperstack.api.assigning_member_role_api import AssigningMemberRoleApi
from hyperstack.api.auth_api import AuthApi
from hyperstack.api.billing_api import BillingApi
from hyperstack.api.callbacks_api import CallbacksApi
from hyperstack.api.compliance_api import ComplianceApi
from hyperstack.api.credit_api import CreditApi
from hyperstack.api.dashboard_api import DashboardApi
from hyperstack.api.deployment_api import DeploymentApi
from hyperstack.api.environment_api import EnvironmentApi
from hyperstack.api.firewall_attachment_api import FirewallAttachmentApi
from hyperstack.api.firewalls_api import FirewallsApi
from hyperstack.api.flavor_api import FlavorApi
from hyperstack.api.floating_ip_api import FloatingIpApi
from hyperstack.api.gpu_api import GpuApi
from hyperstack.api.image_api import ImageApi
from hyperstack.api.invite_api import InviteApi
from hyperstack.api.keypair_api import KeypairApi
from hyperstack.api.organization_api import OrganizationApi
from hyperstack.api.payment_api import PaymentApi
from hyperstack.api.permission_api import PermissionApi
from hyperstack.api.policy_api import PolicyApi
from hyperstack.api.profile_api import ProfileApi
from hyperstack.api.rbac_role_api import RbacRoleApi
from hyperstack.api.region_api import RegionApi
from hyperstack.api.security_rules_api import SecurityRulesApi
from hyperstack.api.stock_api import StockApi
from hyperstack.api.template_api import TemplateApi
from hyperstack.api.user_api import UserApi
from hyperstack.api.user_detail_choice_api import UserDetailChoiceApi
from hyperstack.api.user_permission_api import UserPermissionApi
from hyperstack.api.virtual_machine_api import VirtualMachineApi
from hyperstack.api.virtual_machine_events_api import VirtualMachineEventsApi
from hyperstack.api.vnc_url_api import VncUrlApi
from hyperstack.api.volume_api import VolumeApi
from hyperstack.api.volume_attachment_api import VolumeAttachmentApi

# import ApiClient
from hyperstack.api_response import ApiResponse
from hyperstack.api_client import ApiClient
from hyperstack.configuration import Configuration
from hyperstack.exceptions import OpenApiException
from hyperstack.exceptions import ApiTypeError
from hyperstack.exceptions import ApiValueError
from hyperstack.exceptions import ApiKeyError
from hyperstack.exceptions import ApiAttributeError
from hyperstack.exceptions import ApiException

# import models into sdk package
from hyperstack.models.add_update_flavor_organization_payload import AddUpdateFlavorOrganizationPayload
from hyperstack.models.add_user_info_success_response_model import AddUserInfoSuccessResponseModel
from hyperstack.models.admin_add_update_image_organization_payload import AdminAddUpdateImageOrganizationPayload
from hyperstack.models.admin_bootstrap_environment_payload import AdminBootstrapEnvironmentPayload
from hyperstack.models.admin_cluster_resource import AdminClusterResource
from hyperstack.models.admin_container_resource import AdminContainerResource
from hyperstack.models.admin_contract_event_fields import AdminContractEventFields
from hyperstack.models.admin_contract_fields import AdminContractFields
from hyperstack.models.admin_count_resources_organization import AdminCountResourcesOrganization
from hyperstack.models.admin_count_resources_organizations import AdminCountResourcesOrganizations
from hyperstack.models.admin_create_contract_response_model import AdminCreateContractResponseModel
from hyperstack.models.admin_envrionment_resources import AdminEnvrionmentResources
from hyperstack.models.admin_flavor_detail_fields import AdminFlavorDetailFields
from hyperstack.models.admin_flavor_detail_node_fields import AdminFlavorDetailNodeFields
from hyperstack.models.admin_flavor_resource import AdminFlavorResource
from hyperstack.models.admin_flavor_resources_list import AdminFlavorResourcesList
from hyperstack.models.admin_get_contract_detail_fields import AdminGetContractDetailFields
from hyperstack.models.admin_get_version_response import AdminGetVersionResponse
from hyperstack.models.admin_hibernation_restoration_payload_model import AdminHibernationRestorationPayloadModel
from hyperstack.models.admin_image_admin_fields import AdminImageAdminFields
from hyperstack.models.admin_image_admin_response import AdminImageAdminResponse
from hyperstack.models.admin_image_admin_response_image import AdminImageAdminResponseImage
from hyperstack.models.admin_image_list_admin_response import AdminImageListAdminResponse
from hyperstack.models.admin_instance_resources import AdminInstanceResources
from hyperstack.models.admin_node_resource import AdminNodeResource
from hyperstack.models.admin_organization_resource_list import AdminOrganizationResourceList
from hyperstack.models.admin_organization_resource_response import AdminOrganizationResourceResponse
from hyperstack.models.admin_organization_resources import AdminOrganizationResources
from hyperstack.models.admin_organization_response_model import AdminOrganizationResponseModel
from hyperstack.models.admin_organization_summary_fields import AdminOrganizationSummaryFields
from hyperstack.models.admin_organizations_response_model import AdminOrganizationsResponseModel
from hyperstack.models.admin_organizations_summary_response_model import AdminOrganizationsSummaryResponseModel
from hyperstack.models.admin_user_fields import AdminUserFields
from hyperstack.models.admin_user_response_model import AdminUserResponseModel
from hyperstack.models.admin_users_response_model import AdminUsersResponseModel
from hyperstack.models.admin_version_response_model import AdminVersionResponseModel
from hyperstack.models.admin_volume_resource import AdminVolumeResource
from hyperstack.models.adminaddorganizationpayload import Adminaddorganizationpayload
from hyperstack.models.admincreditpostpayload import Admincreditpostpayload
from hyperstack.models.adminpaymenthistoryfields import Adminpaymenthistoryfields
from hyperstack.models.adminpaymenthistoryresponse import Adminpaymenthistoryresponse
from hyperstack.models.adminrechargehistoryfields import Adminrechargehistoryfields
from hyperstack.models.adminrechargehistoryresponse import Adminrechargehistoryresponse
from hyperstack.models.adminthresholdpostpayload import Adminthresholdpostpayload
from hyperstack.models.api_key_fields import ApiKeyFields
from hyperstack.models.api_key_verify_fields import ApiKeyVerifyFields
from hyperstack.models.assign_rbac_role_payload import AssignRbacRolePayload
from hyperstack.models.attach_callback_payload import AttachCallbackPayload
from hyperstack.models.attach_callback_response import AttachCallbackResponse
from hyperstack.models.attach_firewall_with_vm import AttachFirewallWithVM
from hyperstack.models.attach_firewalls_to_vm_payload import AttachFirewallsToVMPayload
from hyperstack.models.attach_volume_fields import AttachVolumeFields
from hyperstack.models.attach_volumes import AttachVolumes
from hyperstack.models.attach_volumes_payload import AttachVolumesPayload
from hyperstack.models.auth_get_token_response_model import AuthGetTokenResponseModel
from hyperstack.models.auth_request_login_fields import AuthRequestLoginFields
from hyperstack.models.auth_request_login_response_model import AuthRequestLoginResponseModel
from hyperstack.models.auth_user_fields import AuthUserFields
from hyperstack.models.auth_user_info_response_model import AuthUserInfoResponseModel
from hyperstack.models.billing_response import BillingResponse
from hyperstack.models.billingimmuneresources import Billingimmuneresources
from hyperstack.models.billingimmuneresourcesresponse import Billingimmuneresourcesresponse
from hyperstack.models.billingmetricesfields import Billingmetricesfields
from hyperstack.models.billingmetricesresponse import Billingmetricesresponse
from hyperstack.models.common_response_model import CommonResponseModel
from hyperstack.models.compliance_fields import ComplianceFields
from hyperstack.models.compliance_model_fields import ComplianceModelFields
from hyperstack.models.compliance_payload import CompliancePayload
from hyperstack.models.compliance_response import ComplianceResponse
from hyperstack.models.container_overview_fields import ContainerOverviewFields
from hyperstack.models.contract_instance_fields import ContractInstanceFields
from hyperstack.models.contract_instances_response import ContractInstancesResponse
from hyperstack.models.create_contarct_fields import CreateContarctFields
from hyperstack.models.create_contract_payload import CreateContractPayload
from hyperstack.models.create_discount_response import CreateDiscountResponse
from hyperstack.models.create_discounts_payload import CreateDiscountsPayload
from hyperstack.models.create_environment import CreateEnvironment
from hyperstack.models.create_firewall_payload import CreateFirewallPayload
from hyperstack.models.create_firewall_rule_payload import CreateFirewallRulePayload
from hyperstack.models.create_gpu import CreateGPU
from hyperstack.models.create_instances_payload import CreateInstancesPayload
from hyperstack.models.create_profile_payload import CreateProfilePayload
from hyperstack.models.create_profile_response import CreateProfileResponse
from hyperstack.models.create_security_rule_payload import CreateSecurityRulePayload
from hyperstack.models.create_update_compliance_response import CreateUpdateComplianceResponse
from hyperstack.models.create_update_permission_payload import CreateUpdatePermissionPayload
from hyperstack.models.create_update_permission_response_model import CreateUpdatePermissionResponseModel
from hyperstack.models.create_update_policy_payload import CreateUpdatePolicyPayload
from hyperstack.models.create_update_policy_response_model import CreateUpdatePolicyResponseModel
from hyperstack.models.create_update_rbac_role_payload import CreateUpdateRbacRolePayload
from hyperstack.models.create_volume_payload import CreateVolumePayload
from hyperstack.models.customer_contract_detail_response_model import CustomerContractDetailResponseModel
from hyperstack.models.customer_contract_fields import CustomerContractFields
from hyperstack.models.customer_fields import CustomerFields
from hyperstack.models.customer_payload import CustomerPayload
from hyperstack.models.dashboard_info_response import DashboardInfoResponse
from hyperstack.models.deployment_fields import DeploymentFields
from hyperstack.models.deployment_fieldsforstartdeployments import DeploymentFieldsforstartdeployments
from hyperstack.models.deployments import Deployments
from hyperstack.models.detach_volumes import DetachVolumes
from hyperstack.models.detach_volumes_payload import DetachVolumesPayload
from hyperstack.models.discount_entity_model import DiscountEntityModel
from hyperstack.models.discount_fields import DiscountFields
from hyperstack.models.discount_plan_fields import DiscountPlanFields
from hyperstack.models.discount_resource_fields import DiscountResourceFields
from hyperstack.models.editlabelofanexisting_vm_payload import EditlabelofanexistingVMPayload
from hyperstack.models.environment import Environment
from hyperstack.models.environment_fields import EnvironmentFields
from hyperstack.models.environment_fieldsfor_volume import EnvironmentFieldsforVolume
from hyperstack.models.environments import Environments
from hyperstack.models.error_response_model import ErrorResponseModel
from hyperstack.models.excludebillingpostpayload import Excludebillingpostpayload
from hyperstack.models.excludebillingpostresponse import Excludebillingpostresponse
from hyperstack.models.firewall_attachment_model import FirewallAttachmentModel
from hyperstack.models.firewall_attachment_vm_model import FirewallAttachmentVMModel
from hyperstack.models.firewall_detail_fields import FirewallDetailFields
from hyperstack.models.firewall_detail_response import FirewallDetailResponse
from hyperstack.models.firewall_environment_fields import FirewallEnvironmentFields
from hyperstack.models.firewall_fields import FirewallFields
from hyperstack.models.firewall_response import FirewallResponse
from hyperstack.models.firewall_rule import FirewallRule
from hyperstack.models.firewalls_list_response import FirewallsListResponse
from hyperstack.models.flavor_admin_response import FlavorAdminResponse
from hyperstack.models.flavor_admin_response_flavors import FlavorAdminResponseFlavors
from hyperstack.models.flavor_detail_response import FlavorDetailResponse
from hyperstack.models.flavor_fields import FlavorFields
from hyperstack.models.flavor_item_get_response import FlavorItemGetResponse
from hyperstack.models.flavor_list_response import FlavorListResponse
from hyperstack.models.flavor_object_fields import FlavorObjectFields
from hyperstack.models.flavor_payload import FlavorPayload
from hyperstack.models.flavor_response import FlavorResponse
from hyperstack.models.flavor_vm_fields import FlavorVMFields
from hyperstack.models.flavor_vms_response import FlavorVMsResponse
from hyperstack.models.future_node_model import FutureNodeModel
from hyperstack.models.future_node_response_model import FutureNodeResponseModel
from hyperstack.models.future_node_stock_model import FutureNodeStockModel
from hyperstack.models.future_node_update_model import FutureNodeUpdateModel
from hyperstack.models.future_nodes_stock_model import FutureNodesStockModel
from hyperstack.models.gpu import GPU
from hyperstack.models.gpu_fields import GPUFields
from hyperstack.models.gpu_list import GPUList
from hyperstack.models.gpu_region_fields import GPURegionFields
from hyperstack.models.generate_api_key_response_model import GenerateApiKeyResponseModel
from hyperstack.models.get_all_discount_for_all_organization_response import GetAllDiscountForAllOrganizationResponse
from hyperstack.models.get_all_discounts_fields import GetAllDiscountsFields
from hyperstack.models.get_api_key_response_model import GetApiKeyResponseModel
from hyperstack.models.get_contract_detail_response_model import GetContractDetailResponseModel
from hyperstack.models.get_contract_events_response_model import GetContractEventsResponseModel
from hyperstack.models.get_contracts_list_response_model import GetContractsListResponseModel
from hyperstack.models.get_customer_contracts_list_response_model import GetCustomerContractsListResponseModel
from hyperstack.models.get_discount_detail_response import GetDiscountDetailResponse
from hyperstack.models.get_discount_response import GetDiscountResponse
from hyperstack.models.get_entity_discount_detail_response import GetEntityDiscountDetailResponse
from hyperstack.models.get_invites_response_model import GetInvitesResponseModel
from hyperstack.models.get_organization_response_model import GetOrganizationResponseModel
from hyperstack.models.get_permissions_response_model import GetPermissionsResponseModel
from hyperstack.models.get_policies_response_model import GetPoliciesResponseModel
from hyperstack.models.get_rbac_roles_response_model import GetRbacRolesResponseModel
from hyperstack.models.get_token_payload import GetTokenPayload
from hyperstack.models.get_user_permissions_response_model import GetUserPermissionsResponseModel
from hyperstack.models.get_version_response import GetVersionResponse
from hyperstack.models.getcreditandthresholdinfo import Getcreditandthresholdinfo
from hyperstack.models.getcreditandthresholdinfoinresponse import Getcreditandthresholdinfoinresponse
from hyperstack.models.image_fields import ImageFields
from hyperstack.models.image_get_response import ImageGetResponse
from hyperstack.models.image_logos import ImageLogos
from hyperstack.models.images import Images
from hyperstack.models.import_keypair_payload import ImportKeypairPayload
from hyperstack.models.import_keypair_response import ImportKeypairResponse
from hyperstack.models.infrahub_resource_object_response import InfrahubResourceObjectResponse
from hyperstack.models.insert_discount_plan_fields import InsertDiscountPlanFields
from hyperstack.models.instance import Instance
from hyperstack.models.instance_admin import InstanceAdmin
from hyperstack.models.instance_admin_fields import InstanceAdminFields
from hyperstack.models.instance_environment_fields import InstanceEnvironmentFields
from hyperstack.models.instance_events import InstanceEvents
from hyperstack.models.instance_events_fields import InstanceEventsFields
from hyperstack.models.instance_fields import InstanceFields
from hyperstack.models.instance_flavor_fields import InstanceFlavorFields
from hyperstack.models.instance_image_fields import InstanceImageFields
from hyperstack.models.instance_keypair_fields import InstanceKeypairFields
from hyperstack.models.instance_overview_fields import InstanceOverviewFields
from hyperstack.models.instance_resize_payload import InstanceResizePayload
from hyperstack.models.instances import Instances
from hyperstack.models.instances_admin import InstancesAdmin
from hyperstack.models.instances_summary_admin import InstancesSummaryAdmin
from hyperstack.models.instances_summary_fields import InstancesSummaryFields
from hyperstack.models.internal_environment_fields import InternalEnvironmentFields
from hyperstack.models.internal_instance_fields import InternalInstanceFields
from hyperstack.models.internal_instance_flavor_fields import InternalInstanceFlavorFields
from hyperstack.models.internal_instance_image_fields import InternalInstanceImageFields
from hyperstack.models.internal_instance_keypair_fields import InternalInstanceKeypairFields
from hyperstack.models.internal_instances_response import InternalInstancesResponse
from hyperstack.models.internal_security_rules_fields_for_instance import InternalSecurityRulesFieldsForInstance
from hyperstack.models.internal_volume_attachment_fields import InternalVolumeAttachmentFields
from hyperstack.models.internal_volume_fields import InternalVolumeFields
from hyperstack.models.internal_volumes_response import InternalVolumesResponse
from hyperstack.models.invite_fields import InviteFields
from hyperstack.models.invite_user_payload import InviteUserPayload
from hyperstack.models.invite_user_response_model import InviteUserResponseModel
from hyperstack.models.keypair_fields import KeypairFields
from hyperstack.models.keypairs import Keypairs
from hyperstack.models.lable_resonse import LableResonse
from hyperstack.models.lastdaycostfields import Lastdaycostfields
from hyperstack.models.lastdaycostresponse import Lastdaycostresponse
from hyperstack.models.logo_get_response import LogoGetResponse
from hyperstack.models.logout_payload import LogoutPayload
from hyperstack.models.metric_item_fields import MetricItemFields
from hyperstack.models.metrics_fields import MetricsFields
from hyperstack.models.new_configurations_response import NewConfigurationsResponse
from hyperstack.models.new_model_response import NewModelResponse
from hyperstack.models.new_stock_response import NewStockResponse
from hyperstack.models.new_stock_retrive_response import NewStockRetriveResponse
from hyperstack.models.new_stock_update_response_model import NewStockUpdateResponseModel
from hyperstack.models.node_model import NodeModel
from hyperstack.models.node_payload_model import NodePayloadModel
from hyperstack.models.node_power_usage_model import NodePowerUsageModel
from hyperstack.models.node_response_model import NodeResponseModel
from hyperstack.models.node_stock_payload_model import NodeStockPayloadModel
from hyperstack.models.node_stock_response_model import NodeStockResponseModel
from hyperstack.models.node_stocks_payload import NodeStocksPayload
from hyperstack.models.organization_fields import OrganizationFields
from hyperstack.models.organization_object_response import OrganizationObjectResponse
from hyperstack.models.organization_user_response_model import OrganizationUserResponseModel
from hyperstack.models.overview_info import OverviewInfo
from hyperstack.models.payment_details_fields import PaymentDetailsFields
from hyperstack.models.payment_details_response import PaymentDetailsResponse
from hyperstack.models.payment_initiate_fields import PaymentInitiateFields
from hyperstack.models.payment_initiate_payload import PaymentInitiatePayload
from hyperstack.models.payment_initiate_response import PaymentInitiateResponse
from hyperstack.models.permission_fields import PermissionFields
from hyperstack.models.policy_fields import PolicyFields
from hyperstack.models.policy_permission_fields import PolicyPermissionFields
from hyperstack.models.power_usage_model import PowerUsageModel
from hyperstack.models.pricebook_model import PricebookModel
from hyperstack.models.pricebook_resource_object_response import PricebookResourceObjectResponse
from hyperstack.models.profile_fields import ProfileFields
from hyperstack.models.profile_list_response import ProfileListResponse
from hyperstack.models.profile_object_fields import ProfileObjectFields
from hyperstack.models.rbac_role_detail_response_model import RbacRoleDetailResponseModel
from hyperstack.models.rbac_role_field import RbacRoleField
from hyperstack.models.rbac_role_fields import RbacRoleFields
from hyperstack.models.refresh_token_payload import RefreshTokenPayload
from hyperstack.models.region_fields import RegionFields
from hyperstack.models.region_payload import RegionPayload
from hyperstack.models.region_response import RegionResponse
from hyperstack.models.regions import Regions
from hyperstack.models.remove_member_from_organization_response_model import RemoveMemberFromOrganizationResponseModel
from hyperstack.models.remove_member_payload import RemoveMemberPayload
from hyperstack.models.request_console import RequestConsole
from hyperstack.models.resource_payload import ResourcePayload
from hyperstack.models.response_model import ResponseModel
from hyperstack.models.role_permission_fields import RolePermissionFields
from hyperstack.models.role_policy_fields import RolePolicyFields
from hyperstack.models.security_group_rule import SecurityGroupRule
from hyperstack.models.security_group_rule_fields import SecurityGroupRuleFields
from hyperstack.models.security_rules_fieldsfor_instance import SecurityRulesFieldsforInstance
from hyperstack.models.security_rules_protocol_fields import SecurityRulesProtocolFields
from hyperstack.models.set_defaults_payload import SetDefaultsPayload
from hyperstack.models.single_visibility_user_response import SingleVisibilityUserResponse
from hyperstack.models.start_deployment import StartDeployment
from hyperstack.models.start_deployment_payload import StartDeploymentPayload
from hyperstack.models.stock_visibility_user_list_response import StockVisibilityUserListResponse
from hyperstack.models.stock_visibility_user_payload import StockVisibilityUserPayload
from hyperstack.models.success_response_model import SuccessResponseModel
from hyperstack.models.template import Template
from hyperstack.models.template_fields import TemplateFields
from hyperstack.models.templates import Templates
from hyperstack.models.token_fields import TokenFields
from hyperstack.models.update_contract_payload import UpdateContractPayload
from hyperstack.models.update_discounts_payload import UpdateDiscountsPayload
from hyperstack.models.update_discounts_status_payload import UpdateDiscountsStatusPayload
from hyperstack.models.update_environment import UpdateEnvironment
from hyperstack.models.update_gpu import UpdateGPU
from hyperstack.models.update_keypair_name import UpdateKeypairName
from hyperstack.models.update_keypairnameresponse import UpdateKeypairnameresponse
from hyperstack.models.update_organization_payload import UpdateOrganizationPayload
from hyperstack.models.update_organization_response_model import UpdateOrganizationResponseModel
from hyperstack.models.update_template import UpdateTemplate
from hyperstack.models.user_default_choice_for_admin_fields import UserDefaultChoiceForAdminFields
from hyperstack.models.user_default_choice_for_user_fields import UserDefaultChoiceForUserFields
from hyperstack.models.user_default_choices_for_admin_response import UserDefaultChoicesForAdminResponse
from hyperstack.models.user_default_choices_for_user_response import UserDefaultChoicesForUserResponse
from hyperstack.models.user_permission_fields import UserPermissionFields
from hyperstack.models.user_transfer_payload import UserTransferPayload
from hyperstack.models.userinfopostpayload import Userinfopostpayload
from hyperstack.models.users_info_fields import UsersInfoFields
from hyperstack.models.users_info_list_response import UsersInfoListResponse
from hyperstack.models.vncurl import VNCURL
from hyperstack.models.vncurl_fields import VNCURLFields
from hyperstack.models.verify_api_key_payload import VerifyApiKeyPayload
from hyperstack.models.verify_api_key_response_model import VerifyApiKeyResponseModel
from hyperstack.models.volume import Volume
from hyperstack.models.volume_attachment_fields import VolumeAttachmentFields
from hyperstack.models.volume_fields import VolumeFields
from hyperstack.models.volume_fieldsfor_instance import VolumeFieldsforInstance
from hyperstack.models.volume_overview_fields import VolumeOverviewFields
from hyperstack.models.volume_types import VolumeTypes
from hyperstack.models.volumes import Volumes
