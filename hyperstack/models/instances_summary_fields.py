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
from typing import Optional, Set
from typing_extensions import Self

class InstancesSummaryFields(BaseModel):
    """
    InstancesSummaryFields
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    environment: Optional[StrictStr] = None
    org_id: Optional[StrictInt] = None
    environment_id: Optional[StrictInt] = None
    image: Optional[StrictStr] = None
    image_id: Optional[StrictInt] = None
    flavor: Optional[StrictStr] = None
    flavor_id: Optional[StrictInt] = None
    keypair: Optional[StrictStr] = None
    keypair_id: Optional[StrictInt] = None
    fixed_ip: Optional[StrictStr] = None
    floating_ip: Optional[StrictStr] = None
    floating_ip_status: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["id", "name", "environment", "org_id", "environment_id", "image", "image_id", "flavor", "flavor_id", "keypair", "keypair_id", "fixed_ip", "floating_ip", "floating_ip_status", "status", "created_at", "updated_at"]

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
        """Create an instance of InstancesSummaryFields from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InstancesSummaryFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "environment": obj.get("environment"),
            "org_id": obj.get("org_id"),
            "environment_id": obj.get("environment_id"),
            "image": obj.get("image"),
            "image_id": obj.get("image_id"),
            "flavor": obj.get("flavor"),
            "flavor_id": obj.get("flavor_id"),
            "keypair": obj.get("keypair"),
            "keypair_id": obj.get("keypair_id"),
            "fixed_ip": obj.get("fixed_ip"),
            "floating_ip": obj.get("floating_ip"),
            "floating_ip_status": obj.get("floating_ip_status"),
            "status": obj.get("status"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


