from pydantic import BaseModel, Field, validator

from app.utils import normalize_title


class CardsSchema(BaseModel):
    title: str = Field(max_length=30, min_length=8, default=None)
    type: str
    description: str = Field(max_length=200, min_length=8, default=None)
    category: str = None

    @validator("type")
    @classmethod
    def type_must_contain_allow(cls, obj: str) -> str:
        _allow_type = ["issue", "bug", "task"]
        if normalize_title(obj) not in _allow_type:
            raise ValueError(f"Type allow {_allow_type}")
        return obj

    @validator("category")
    @classmethod
    def category_must_contain_allow(cls, obj: str) -> str:
        _allow_category = ["maintenance", "research", "test"]
        if normalize_title(obj) not in _allow_category:
            raise ValueError(f"Type category {_allow_category}")
        return obj


class BaseCardsSchema(BaseModel):
    type: str


class CardsIssueSchema(BaseCardsSchema):
    title: str = Field(max_length=30, min_length=8)
    description: str


class CardsBugSchema(BaseCardsSchema):
    description: str


class CardsTaskSchema(BaseCardsSchema):
    title: str = Field(max_length=30, min_length=8)
    category: str
