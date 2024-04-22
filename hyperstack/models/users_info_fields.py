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
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UsersInfoFields(BaseModel):
    """
    UsersInfoFields
    """ # noqa: E501
    id: Optional[StrictInt] = None
    organization_id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    business: Optional[StrictBool] = None
    company_name: Optional[StrictStr] = None
    vat_number: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    billing_address1: Optional[StrictStr] = None
    billing_address2: Optional[StrictStr] = None
    zip_code: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["id", "organization_id", "name", "email", "business", "company_name", "vat_number", "phone", "billing_address1", "billing_address2", "zip_code", "country", "state", "created_at"]

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
        """Create an instance of UsersInfoFields from a JSON string"""
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
        """Create an instance of UsersInfoFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "organization_id": obj.get("organization_id"),
            "name": obj.get("name"),
            "email": obj.get("email"),
            "business": obj.get("business"),
            "company_name": obj.get("company_name"),
            "vat_number": obj.get("vat_number"),
            "phone": obj.get("phone"),
            "billing_address1": obj.get("billing_address1"),
            "billing_address2": obj.get("billing_address2"),
            "zip_code": obj.get("zip_code"),
            "country": obj.get("country"),
            "state": obj.get("state"),
            "created_at": obj.get("created_at")
        })
        return _obj


