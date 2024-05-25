import os


def Config():
    return {
        'port': os.getenv('PORT', 3000),
        'redis': {
            'host': os.getenv('REDIS_HOST', 'localhost'),
            'port': os.getenv('REDIS_PORT', 6379)
        }
    }