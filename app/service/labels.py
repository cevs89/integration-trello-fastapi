from dataclasses import dataclass, field

import requests

from app.config import settings
from app.utils import QUERY_BASE


@dataclass
class LabelsService:
    id_board: str
    _label_dict: dict = field(default_factory=dict)

    def __set_labels(self) -> dict:
        _labels_create = {
            "Bug": "red",
            "Maintenance": "blue",
            "Research": "green",
            "Test": "yellow",
        }
        return _labels_create

    def __requests_endpoint(self, _params: dict):
        endpoint_label = settings.BASE_URL + f"/boards/{self.id_board}/labels"

        _response = requests.request("POST", endpoint_label, params=_params)
        if _response.status_code == 200:
            _data = _response.json()
            self._label_dict[_params["name"]] = _data["id"]
            return True
        else:
            raise ValueError(_response.text)

    @property
    def execute(self):
        for _name, _color in self.__set_labels().items():
            QUERY_BASE["name"] = _name
            QUERY_BASE["color"] = _color
            self.__requests_endpoint(QUERY_BASE)

        return self._label_dict
