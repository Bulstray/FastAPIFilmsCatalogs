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

    redis.delete("name")
    print(redis.get("name"))
    1 + ''

    print(redis.get("name"))
    print("spam", redis.get("spam"))

    return None


if __name__ == "__main__":
    main()
