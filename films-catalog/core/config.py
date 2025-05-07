import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MOVIE_STORAGE_FILEPATH = BASE_DIR / "movie.json"


LOG_LEVEL = logging.INFO
LOG_FORMAT: str = (
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)

API_TOKENS = frozenset(
    {
        "nWkE1Wd-_TUBP493xjRXng",
        "Gw28yx5gjLQHa0I4REEDGQ",
    },
)


USERS_DB: dict[str, str] = {
    "sam": "password",
    "bob": "qwerty",
}


REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_DB_TOKENS = 1

REDIS_TOKES_SET_NAME = "tokens"
