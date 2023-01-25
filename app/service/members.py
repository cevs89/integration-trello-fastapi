from dataclasses import dataclass, field
from typing import List

import requests
from sqlalchemy.orm import Session

from app.config import settings
from app.controller import update_data
from app.utils import QUERY_BASE


@dataclass
class MembersService:
    db: Session
    id_board: str
    _list_members: List = field(default_factory=list)

    def __requests_endpoint(self):
        endpoint_members = settings.BASE_URL + f"/boards/{self.id_board}/members"

        _response = requests.request("GET", endpoint_members, params=QUERY_BASE)
        if _response.status_code == 200:
            _data = _response.json()
            self._list_members = [i["id"] for i in _data]
            return True
        else:
            raise ValueError(_response.text)

    @property
    def execute(self):
        self.__requests_endpoint()
        update_data(self.db, self._list_members)
        return self._list_members
