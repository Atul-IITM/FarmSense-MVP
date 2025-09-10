import httpx
import hashlib
import json
import datetime
import os
from ..services.cache import cache_get, cache_set

# Fetch API keys from environment variables
AM_BEE_API_KEY = os.environ.get("AM_BEE_API_KEY")
BASE_URL = "https://api.ambee.com/agri-weather"

async def get_forecast(lat: float, lon: float):
    """
    Fetches 7-day weather forecast from Ambee Agri Weather API with caching.
    """
    if not AM_BEE_API_KEY:
        raise ValueError("AM_BEE_API_KEY environment variable is not set.")

    # Create a unique cache key based on geo-hash and date
    key = f"weather:{round(lat, 3)}:{round(lon, 3)}:{datetime.date.today()}"
    h = hashlib.md5(key.encode()).hexdigest()
    cached = await cache_get(h)
    
    if cached:
        print("Using cached weather data.")
        return json.loads(cached)
    
    headers = {"x-api-key": AM_BEE_API_KEY}
    params = {"lat": lat, "lon": lon}
    
    async with httpx.AsyncClient(timeout=10) as client:
        try:
            r = await client.get(BASE_URL, headers=headers, params=params)
            r.raise_for_status()
            data = r.json()
            
            # Cache the data for 6 hours
            await cache_set(h, json.dumps(data), ttl=6 * 3600)
            
            return data
        except httpx.HTTPStatusError as e:
            print(f"HTTP error fetching weather data: {e.response.status_code}")
            raise Exception(f"Weather API error: {e.response.status_code}")
        except httpx.RequestError as e:
            print(f"Request error fetching weather data: {e}")
            raise Exception("Could not connect to the weather API.")