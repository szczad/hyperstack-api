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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from hyperstack.models.admin_get_contract_detail_fields import AdminGetContractDetailFields
from hyperstack.models.discount_plan_fields import DiscountPlanFields
from typing import Optional, Set
from typing_extensions import Self

class GetContractDetailResponseModel(BaseModel):
    """
    GetContractDetailResponseModel
    """ # noqa: E501
    status: Optional[StrictBool] = None
    message: Optional[StrictStr] = None
    contract: Optional[AdminGetContractDetailFields] = None
    discount_plans: Optional[List[DiscountPlanFields]] = None
    __properties: ClassVar[List[str]] = ["status", "message", "contract", "discount_plans"]

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
        """Create an instance of GetContractDetailResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of contract
        if self.contract:
            _dict['contract'] = self.contract.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in discount_plans (list)
        _items = []
        if self.discount_plans:
            for _item in self.discount_plans:
                if _item:
                    _items.append(_item.to_dict())
            _dict['discount_plans'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetContractDetailResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "message": obj.get("message"),
            "contract": AdminGetContractDetailFields.from_dict(obj["contract"]) if obj.get("contract") is not None else None,
            "discount_plans": [DiscountPlanFields.from_dict(_item) for _item in obj["discount_plans"]] if obj.get("discount_plans") is not None else None
        })
        return _obj


