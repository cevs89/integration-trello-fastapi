from pydantic import BaseModel, Field


class BoardSchema(BaseModel):
    name_board: str = Field(max_length=20, min_length=8)
