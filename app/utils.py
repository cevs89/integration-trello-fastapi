from app.config import settings

QUERY_BASE = {"key": settings.KEY_AUTH, "token": settings.TOKEN_AUTH}


def normalize_title(_title):
    return _title.lower().strip()
