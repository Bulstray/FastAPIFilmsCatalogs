from typing import cast

from redis import Redis

from core import config

from .users_helper import AbstractUserHelper


class RedisUsersHelper(AbstractUserHelper):

    def __init__(
        self,
        host: str,
        port: int,
        db: int,
    ) -> None:
        self.redis = Redis(host=host, port=port, db=db, decode_responses=True)

    def get_user_password(
        self,
        username: str,
    ) -> str | None:
        return cast(str | None, self.redis.get(name=username))


redis_users = RedisUsersHelper(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB_USERS,
)
