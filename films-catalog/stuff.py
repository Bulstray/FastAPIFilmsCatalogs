from redis import Redis

from core import config

redis = Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB,
    decode_responses=True,
)


def main():
    redis.set("name", "Ramil")
    print(redis.get("name"))

    redis.delete("name")
    print(redis.get("name"))


if __name__ == "__main__":
    main()
