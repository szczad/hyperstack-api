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
from typing import Optional, Set
from typing_extensions import Self

class Billingmetricesfields(BaseModel):
    """
    Billingmetricesfields
    """ # noqa: E501
    resource_id: Optional[StrictInt] = None
    resource_type: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    organization_id: Optional[StrictInt] = None
    bill_per_minute: Optional[Union[StrictFloat, StrictInt]] = None
    create_time: Optional[datetime] = None
    terminate_time: Optional[datetime] = None
    total_up_time: Optional[Union[StrictFloat, StrictInt]] = None
    total_bill: Optional[Union[StrictFloat, StrictInt]] = None
    active: Optional[StrictBool] = None
    exclude_billing: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["resource_id", "resource_type", "name", "organization_id", "bill_per_minute", "create_time", "terminate_time", "total_up_time", "total_bill", "active", "exclude_billing"]

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
        """Create an instance of Billingmetricesfields from a JSON string"""
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
        """Create an instance of Billingmetricesfields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "resource_id": obj.get("resource_id"),
            "resource_type": obj.get("resource_type"),
            "name": obj.get("name"),
            "organization_id": obj.get("organization_id"),
            "bill_per_minute": obj.get("bill_per_minute"),
            "create_time": obj.get("create_time"),
            "terminate_time": obj.get("terminate_time"),
            "total_up_time": obj.get("total_up_time"),
            "total_bill": obj.get("total_bill"),
            "active": obj.get("active"),
            "exclude_billing": obj.get("exclude_billing")
        })
        return _obj


