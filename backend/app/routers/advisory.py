from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel
from typing import Optional
from ..services import weather as weather_service
from ..logic import advisory as advisory_logic

router = APIRouter()

class AdvisoryQuery(BaseModel):
    lat: float
    lon: float
    question: Optional[str]

@router.post("/advisory/query")
async def get_advisory(query: AdvisoryQuery):
    """
    Accepts a natural language query and returns structured advice.
    This is an MVP-level implementation.
    """
    # In a more advanced version, a language model would process the 'question'
    # and use it to call the appropriate internal functions.
    
    # For this MVP, we will only use lat/lon to generate a weather-based advisory.
    
    try:
        weather_data = await weather_service.get_forecast(query.lat, query.lon)
        spraying_alert = advisory_logic.spraying_guard(weather_data)
        
        # This is a simple logic. In a real system, you'd have many rules
        # and combine their outputs.
        
        if spraying_alert:
            return spraying_alert
        
        return {
            "type": "general_advice",
            "severity": "info",
            "text": "The weather looks clear for farming activities today. No specific alerts at this moment.",
            "reason": "No weather thresholds were breached.",
            "source": "Weather+rules"
        }
        
    except Exception as e:
        return {
            "type": "error",
            "text": f"An error occurred while fetching advisory: {str(e)}",
            "reason": "API call failed or data is unavailable.",
            "source": "System"
        }

@router.get("/weather")
async def get_weather_alerts(lat: float, lon: float):
    """
    Provides a 7-day weather summary with actionable alerts.
    """
    try:
        weather_data = await weather_service.get_forecast(lat, lon)
        alerts = []
        
        # Apply MVP advisory rules
        spraying_alert = advisory_logic.spraying_guard(weather_data)
        if spraying_alert:
            alerts.append(spraying_alert)

        # You would add more rules here (e.g., heat, humidity, etc.)
        
        return {
            "summary": "7-day forecast summary",
            "data": weather_data,
            "alerts": alerts
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))