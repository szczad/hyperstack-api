# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from hyperstack.models.admin_flavor_detail_node_fields import AdminFlavorDetailNodeFields
from typing import Optional, Set
from typing_extensions import Self

class AdminFlavorDetailFields(BaseModel):
    """
    AdminFlavorDetailFields
    """ # noqa: E501
    id: Optional[StrictInt] = None
    openstack_id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    region_name: Optional[StrictStr] = None
    cpu: Optional[StrictInt] = None
    ram: Optional[Union[StrictFloat, StrictInt]] = None
    disk: Optional[StrictInt] = None
    gpu: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    gpu_count: Optional[StrictInt] = None
    stock_available: Optional[StrictBool] = None
    nodes: Optional[List[AdminFlavorDetailNodeFields]] = None
    vms: Optional[List[StrictInt]] = None
    is_public: Optional[StrictBool] = None
    is_custom: Optional[StrictBool] = None
    org_ids: Optional[List[StrictInt]] = None
    ephemeral: Optional[StrictInt] = None
    description: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["id", "openstack_id", "name", "region_name", "cpu", "ram", "disk", "gpu", "status", "gpu_count", "stock_available", "nodes", "vms", "is_public", "is_custom", "org_ids", "ephemeral", "description", "created_at"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AdminFlavorDetailFields from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in nodes (list)
        _items = []
        if self.nodes:
            for _item in self.nodes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nodes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdminFlavorDetailFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "openstack_id": obj.get("openstack_id"),
            "name": obj.get("name"),
            "region_name": obj.get("region_name"),
            "cpu": obj.get("cpu"),
            "ram": obj.get("ram"),
            "disk": obj.get("disk"),
            "gpu": obj.get("gpu"),
            "status": obj.get("status"),
            "gpu_count": obj.get("gpu_count"),
            "stock_available": obj.get("stock_available"),
            "nodes": [AdminFlavorDetailNodeFields.from_dict(_item) for _item in obj["nodes"]] if obj.get("nodes") is not None else None,
            "vms": obj.get("vms"),
            "is_public": obj.get("is_public"),
            "is_custom": obj.get("is_custom"),
            "org_ids": obj.get("org_ids"),
            "ephemeral": obj.get("ephemeral"),
            "description": obj.get("description"),
            "created_at": obj.get("created_at")
        })
        return _obj


