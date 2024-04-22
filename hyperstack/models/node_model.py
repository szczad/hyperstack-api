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
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from hyperstack.models.node_stocks_payload import NodeStocksPayload
from typing import Optional, Set
from typing_extensions import Self

class NodeModel(BaseModel):
    """
    NodeModel
    """ # noqa: E501
    openstack_id: StrictStr
    openstack_name: Optional[StrictStr] = None
    nexgen_name: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    provision_date: Optional[datetime] = None
    sunset_date: Optional[datetime] = None
    flavors: Optional[List[StrictStr]] = None
    projects: Optional[List[StrictStr]] = None
    stocks: Optional[List[NodeStocksPayload]] = None
    organizations: Optional[List[StrictInt]] = None
    __properties: ClassVar[List[str]] = ["openstack_id", "openstack_name", "nexgen_name", "status", "provision_date", "sunset_date", "flavors", "projects", "stocks", "organizations"]

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
        """Create an instance of NodeModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in stocks (list)
        _items = []
        if self.stocks:
            for _item in self.stocks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['stocks'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NodeModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "openstack_id": obj.get("openstack_id"),
            "openstack_name": obj.get("openstack_name"),
            "nexgen_name": obj.get("nexgen_name"),
            "status": obj.get("status"),
            "provision_date": obj.get("provision_date"),
            "sunset_date": obj.get("sunset_date"),
            "flavors": obj.get("flavors"),
            "projects": obj.get("projects"),
            "stocks": [NodeStocksPayload.from_dict(_item) for _item in obj["stocks"]] if obj.get("stocks") is not None else None,
            "organizations": obj.get("organizations")
        })
        return _obj


