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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from hyperstack.models.admin_contract_event_fields import AdminContractEventFields
from typing import Optional, Set
from typing_extensions import Self

class GetContractEventsResponseModel(BaseModel):
    """
    GetContractEventsResponseModel
    """ # noqa: E501
    status: Optional[StrictBool] = None
    message: Optional[StrictStr] = None
    contract_events: Optional[List[AdminContractEventFields]] = None
    count: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["status", "message", "contract_events", "count"]

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
        """Create an instance of GetContractEventsResponseModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in contract_events (list)
        _items = []
        if self.contract_events:
            for _item in self.contract_events:
                if _item:
                    _items.append(_item.to_dict())
            _dict['contract_events'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetContractEventsResponseModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "message": obj.get("message"),
            "contract_events": [AdminContractEventFields.from_dict(_item) for _item in obj["contract_events"]] if obj.get("contract_events") is not None else None,
            "count": obj.get("count")
        })
        return _obj


