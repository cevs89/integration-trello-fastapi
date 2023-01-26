import ast
import re
import secrets
from dataclasses import dataclass

import requests
from lorem.text import TextLorem
from sqlalchemy.orm import Session

from app.config import settings
from app.controller import get_data
from app.service.members import MembersService
from app.utils import QUERY_BASE, normalize_title
from app.validators import CardsBugSchema, CardsIssueSchema, CardsTaskSchema

ENDPOINT_CARD = settings.BASE_URL + "/cards/"


@dataclass
class CardsService:
    object_board: dict
    db: Session
    query: dict = None

    @property
    def queryset(self):
        return get_data(self.db)

    def __get_label(self):

        _labels = ast.literal_eval(self.queryset.list_labels)

        if normalize_title(self.object_board.type) in ["bug"]:
            _label_get = self.object_board.type
            return _labels[normalize_title(_label_get).capitalize()]

        elif normalize_title(self.object_board.type) in ["task"]:
            _label_category = self.object_board.category
            return _labels[normalize_title(_label_category).capitalize()]
        else:
            return None

    def __get_name_card(self):
        if self.object_board.title:
            return self.object_board.title
        else:
            desing_text = TextLorem(wsep="", srange=(3, 4), words="A B C D".split())
            _text_name = re.sub(r'[.,"\'-?:!;]', "", desing_text.sentence())

            _name_bug = f"bug-{_text_name}-{secrets.randbelow(100)}"
            return _name_bug

    def __get_member(self):

        if normalize_title(self.object_board.type) == "bug":
            if not self.queryset.list_users:
                _list_users = MembersService(self.db, self.queryset.id_board).execute
            else:
                _list_users = ast.literal_eval(self.queryset.list_users)

            if len(_list_users) == 0:
                raise ValueError("You don't have any members in Trello!")

            _randon_user = secrets.choice(_list_users)
            return _randon_user
        else:
            return None

    def __params(self):
        QUERY_BASE["idList"] = self.queryset.id_list
        QUERY_BASE["desc"] = self.object_board.description
        QUERY_BASE["idLabels"] = self.__get_label()
        QUERY_BASE["name"] = self.__get_name_card()
        QUERY_BASE["idMembers"] = self.__get_member()
        self.query = QUERY_BASE

    def __validations(self):
        _type_validate = normalize_title(self.object_board.type)

        if _type_validate == "issue":
            try:
                CardsIssueSchema(**dict(self.object_board))
            except Exception as e:
                raise Exception(e) from e

        elif _type_validate == "bug":
            try:
                CardsBugSchema(**dict(self.object_board))
            except Exception as e:
                raise Exception(e) from e
        else:
            try:
                CardsTaskSchema(**dict(self.object_board))
            except Exception as e:
                raise Exception(e) from e

    def __requests_endpoint(self):
        _response = requests.request("POST", ENDPOINT_CARD, params=self.query)
        if _response.status_code == 200:
            return _response.json()
        else:
            raise ValueError(_response.text)

    @property
    def execute(self):
        self.__validations()
        self.__params()

        _reponse = self.__requests_endpoint()
        return _reponse
