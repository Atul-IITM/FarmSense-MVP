import redis.asyncio as redis
import os

# Get Redis host from environment variables
REDIS_HOST = os.environ.get("REDIS_HOST", "redis")

# Connect to Redis
redis_client = redis.Redis(host=REDIS_HOST, port=6379, db=0, decode_responses=True)

async def cache_get(key: str):
    """Retrieves a value from the cache."""
    return await redis_client.get(key)

async def cache_set(key: str, value, ttl: int = None):
    """Sets a value in the cache with an optional time-to-live."""
    await redis_client.set(key, value, ex=ttl)