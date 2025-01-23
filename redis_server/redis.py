from redis import Redis

from config import RedisSettings


class RedisServer:
    def __init__(self):
        self.server = Redis(RedisSettings.HOST, port=RedisSettings.PORT)
