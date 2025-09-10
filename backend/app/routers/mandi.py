from fastapi import APIRouter, Query
from ..services import mandi as mandi_service

router = APIRouter()

@router.get("/mandi")
async def get_mandi_prices(commodity: str = Query(..., description="e.g., 'Tomato'"), state: str = Query(..., description="e.g., 'Delhi'")):
    """
    Fetches the latest mandi prices for a given commodity and state.
    """
    prices = await mandi_service.get_prices(commodity, state)
    
    # In a real app, you'd process and format this data
    if not prices or 'records' not in prices:
        return {"message": "No data found for this query."}
    
    latest_price = prices['records'][0] if prices['records'] else None

    return {
        "commodity": commodity,
        "state": state,
        "latest_price": latest_price,
        "last_14_day_trend": prices['records'][:14] # For a simple trend display
    }