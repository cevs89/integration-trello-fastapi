import json

from app.models import DataIntegration


def get_data(db):
    return db.query(DataIntegration).first()


def update_data(db, _data_update):
    _db_data_update = db.query(DataIntegration).one_or_none()
    if _db_data_update is None:
        return ValueError("Error Update DataIntegration")

    try:
        _db_data_update.list_users = str(_data_update)

        db.add(_db_data_update)
        db.commit()
        db.refresh(_db_data_update)
    except ConnectionError as exc:
        db.rollback()
        raise RuntimeError(exc) from exc

    return _db_data_update


def create_data(db, payload):
    queryset = DataIntegration

    try:
        db_data = queryset(
            id_board=payload["Board"]["id_board"],
            id_list=payload["lists"]["TO-DO"],
            list_labels=json.dumps(payload["Labels"]),
        )
        db.add(db_data)
        db.commit()
        db.refresh(db_data)
    except ConnectionError as exc:
        db.rollback()
        raise RuntimeError(exc) from exc

    return {"status": "success"}
