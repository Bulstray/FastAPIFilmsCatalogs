from redis import Redis

from core.config import settings

redis = Redis(
    host=settings.redis.connection.host,
    port=settings.redis.connection.port,
    db=settings.redis.db.default,
    decode_responses=True,
)


def main() -> None:
    redis.set("name", "Ramil")
    print(redis.get("name"))

    redis.delete("name")
    print(redis.get("name"))

    return None


if __name__ == "__main__":
    main()
