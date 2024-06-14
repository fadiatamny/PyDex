import os

Config = {
    'port': os.getenv('PORT', 3000),
    'redis': {
        'host': os.getenv('REDIS_HOST', 'localhost'),
        'port': os.getenv('REDIS_PORT', 6379),
        'active': os.getenv('DISABLE_CACHE', 'true') == 'true'
    }
}
