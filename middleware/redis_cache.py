from typing import Any

import redis

from config import RedisSettings


class RedisCache:
    def __init__(self):
        self.server = redis.Redis(host=RedisSettings.HOST, port=RedisSettings.PORT)
