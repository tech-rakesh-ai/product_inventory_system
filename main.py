from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_limiter import FastAPILimiter
import redis.asyncio as redis
import uvicorn
from fastapi import FastAPI
from core.apps.products import views as product_views

app = FastAPI(title="Product Inventory System")

app.include_router(product_views.router)


async def startup_event():
    # Connect to Redis server
    redis_connection = redis.from_url("redis://localhost:6379", encoding="utf-8", decode_responses=True)

    # Initialize FastAPI Cache with Redis backend
    FastAPICache.init(RedisBackend(redis_connection), prefix="fastapi-cache")

    # Initialize FastAPI Limiter with Redis connection
    await FastAPILimiter.init(redis_connection)


# Use the FastAPI instance to add the event handler
app.add_event_handler("startup", startup_event)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, log_level="debug")
