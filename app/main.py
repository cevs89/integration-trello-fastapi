from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from app.controller import create_data
from app.service import BoardService, CardsService
from app.validators import BoardSchema, CardsSchema

from .database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/create/new/environment/", status_code=status.HTTP_201_CREATED)
async def create_environment(get_board: BoardSchema, db: Session = Depends(get_db)):
    try:
        _response = BoardService(get_board).execute
    except Exception as e:
        raise HTTPException from e

    create_data(db, _response)
    return {"details": "Success", "reponse": _response}


@app.post("/create/cards/", status_code=status.HTTP_201_CREATED)
async def create_cards(get_cards: CardsSchema, db: Session = Depends(get_db)):
    try:
        _reponse = CardsService(get_cards, db).execute
    except Exception as e:
        raise HTTPException from e

    return {"details": _reponse}
