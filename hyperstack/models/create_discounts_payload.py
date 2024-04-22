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
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from hyperstack.models.customer_payload import CustomerPayload
from hyperstack.models.resource_payload import ResourcePayload
from typing import Optional, Set
from typing_extensions import Self

class CreateDiscountsPayload(BaseModel):
    """
    CreateDiscountsPayload
    """ # noqa: E501
    customers: List[CustomerPayload]
    discount_resources: List[ResourcePayload]
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    discount_status: StrictStr
    __properties: ClassVar[List[str]] = ["customers", "discount_resources", "start_date", "end_date", "discount_status"]

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
        """Create an instance of CreateDiscountsPayload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in customers (list)
        _items = []
        if self.customers:
            for _item in self.customers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in discount_resources (list)
        _items = []
        if self.discount_resources:
            for _item in self.discount_resources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['discount_resources'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateDiscountsPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customers": [CustomerPayload.from_dict(_item) for _item in obj["customers"]] if obj.get("customers") is not None else None,
            "discount_resources": [ResourcePayload.from_dict(_item) for _item in obj["discount_resources"]] if obj.get("discount_resources") is not None else None,
            "start_date": obj.get("start_date"),
            "end_date": obj.get("end_date"),
            "discount_status": obj.get("discount_status")
        })
        return _obj


