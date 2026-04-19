
import redis
from config.config import settings


def get_redis() -> redis.Redis:
    url = f'redis://:{settings.REDIS_PASSWORD}@redis:6379/3'
    client = redis.from_url(url)

    return client
