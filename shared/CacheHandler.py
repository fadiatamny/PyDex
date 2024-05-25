from redis import Redis
from .Config import Config

class CacheHandler:
    _instance = None

    @staticmethod
    def create():
        if (CacheHandler._instance is None):
            CacheHandler._instance = CacheHandler()
        return CacheHandler._instance

    def __init__(self):
        config = Config()
        host = config['redis']['host']
        port = config['redis']['port']
        self.redis = Redis(host=host, port=port)

    def set(self, key: str, value: str):
        self.redis.set(key, value)

    def get(self, key: str):
        return self.redis.get(key)

    def delete(self, key: str):
        self.redis.delete(key)