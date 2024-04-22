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
from hyperstack.models.organization_user_response_model import OrganizationUserResponseModel
from typing import Optional, Set
from typing_extensions import Self

class OrganizationFields(BaseModel):
    """
    OrganizationFields
    """ # noqa: E501
    id: StrictInt
    name: StrictStr
    credit: Optional[StrictInt] = None
    threshold: Optional[StrictInt] = None
    total_instances: Optional[StrictInt] = None
    total_volumes: Optional[StrictInt] = None
    total_containers: Optional[StrictInt] = None
    total_clusters: Optional[StrictInt] = None
    users: Optional[List[OrganizationUserResponseModel]] = None
    created_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["id", "name", "credit", "threshold", "total_instances", "total_volumes", "total_containers", "total_clusters", "users", "created_at"]

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
        """Create an instance of OrganizationFields from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item in self.users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['users'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrganizationFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "credit": obj.get("credit"),
            "threshold": obj.get("threshold"),
            "total_instances": obj.get("total_instances"),
            "total_volumes": obj.get("total_volumes"),
            "total_containers": obj.get("total_containers"),
            "total_clusters": obj.get("total_clusters"),
            "users": [OrganizationUserResponseModel.from_dict(_item) for _item in obj["users"]] if obj.get("users") is not None else None,
            "created_at": obj.get("created_at")
        })
        return _obj

