import json
from dataclasses import dataclass

import requests

from app.config import settings
from app.service.labels import LabelsService
from app.service.lists import ListsService
from app.utils import QUERY_BASE

ENDPOINT_BOARD = settings.BASE_URL + "/boards/"


@dataclass
class BoardService:
    object_board: dict
    query: dict = None

    def __params(self):
        QUERY_BASE["name"] = self.object_board.name_board
        QUERY_BASE["defaultLists"] = json.dumps(False)
        QUERY_BASE["defaultLabels"] = json.dumps(False)

        self.query = QUERY_BASE

    def __validations(self, data_valid: dict):
        _data_id = data_valid["shortUrl"].split("/")
        _id_board_get = _data_id[::-1][0]
        return _id_board_get

    def __requests_endpoint(self):
        self.__params()

        _response = requests.request("POST", ENDPOINT_BOARD, params=self.query)
        if _response.status_code == 200:
            _reponse_id_board = self.__validations(_response.json())
            return _reponse_id_board
        else:
            raise ValueError(_response.text)

    @property
    def execute(self):
        _reponse_id_board = self.__requests_endpoint()
        _reponse_labels = LabelsService(_reponse_id_board).execute
        _reponse_lists = ListsService(_reponse_id_board).execute

        _reponse_array = {
            "Board": {
                "name": self.object_board.name_board,
                "id_board": _reponse_id_board,
            },
            "Labels": _reponse_labels,
            "lists": _reponse_lists,
        }

        return _reponse_array
