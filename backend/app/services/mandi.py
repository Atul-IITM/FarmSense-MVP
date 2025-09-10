import httpx
import os
from typing import List, Dict

# Fetch API key from environment variables
DATA_GOV_API_KEY = os.environ.get("DATA_GOV_API_KEY")
DATA_GOV_RESOURCE_URL = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"

async def get_prices(commodity: str, state: str) -> Dict:
    """
    Fetches mandi prices from the data.gov.in API.
    """
    if not DATA_GOV_API_KEY:
        raise ValueError("DATA_GOV_API_KEY environment variable is not set.")

    params = {
        "api-key": DATA_GOV_API_KEY,
        "format": "json",
        "limit": 1000,
        "filters[commodity]": commodity.lower(),
        "filters[state]": state.lower(),
        "sort[date]": "desc"
    }

    async with httpx.AsyncClient(timeout=15) as client:
        try:
            r = await client.get(DATA_GOV_RESOURCE_URL, params=params)
            r.raise_for_status()
            return r.json()
        except httpx.HTTPStatusError as e:
            print(f"HTTP error fetching mandi data: {e.response.status_code}")
            raise Exception(f"Mandi API error: {e.response.status_code}")
        except httpx.RequestError as e:
            print(f"Request error fetching mandi data: {e}")
            raise Exception("Could not connect to the mandi price API.")