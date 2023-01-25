from dataclasses import dataclass, field

import requests

from app.config import settings
from app.utils import QUERY_BASE


@dataclass
class ListsService:
    id_board: str
    _list_dict: dict = field(default_factory=dict)

    def __set_lists(self) -> dict:
        _dict_create = {
            "TO-DO": "top",
            "IN PROGRESS": "bottom",
            "REVIEW": "bottom",
            "CLOSED": "bottom",
        }
        return _dict_create

    def __requests_endpoint(self, _params: dict):
        endpoint_list = settings.BASE_URL + f"/boards/{self.id_board}/lists"

        _response = requests.request("POST", endpoint_list, params=_params)
        if _response.status_code == 200:
            _data = _response.json()
            self._list_dict[_params["name"]] = _data["id"]
            return True
        else:
            raise ValueError(_response.text)

    @property
    def execute(self):
        for _name, _positions in self.__set_lists().items():
            QUERY_BASE["name"] = _name
            QUERY_BASE["pos"] = _positions
            self.__requests_endpoint(QUERY_BASE)

        return self._list_dict
