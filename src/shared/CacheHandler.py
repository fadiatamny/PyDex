from redis import Redis
from .Config import Config

class CacheHandler:
    active = Config['redis']['active']

    _instance = None

    @staticmethod
    def create():
        if (CacheHandler._instance is None):
            CacheHandler._instance = CacheHandler()
        return CacheHandler._instance

    def __init__(self):
        host = Config['redis']['host']
        port = Config['redis']['port']
        self.redis = Redis(host=host, port=port)

    def set(self, key: str, value: str):
        if not CacheHandler.active:
            return

        self.redis.set(key, value)

    def get(self, key: str):
        if not CacheHandler.active:
            return

        return self.redis.get(key)

    def delete(self, key: str):
        if not CacheHandler.active:
            return

        self.redis.delete(key)
