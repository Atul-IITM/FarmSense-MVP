from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class FarmerCreate(BaseModel):
    phone: str
    language: str
    location_lat: float
    location_lon: float

# This would be a real database session in a production app
# We'll use a simple in-memory list for this MVP
db_farmers = []
db_farms = []

@router.post("/signup", status_code=201)
async def signup(farmer_data: FarmerCreate):
    """
    Registers a new farmer and their first farm.
    """
    # In a real app, you would check if the phone number already exists
    if any(f['phone'] == farmer_data.phone for f in db_farmers):
        raise HTTPException(status_code=400, detail="Phone number already registered")

    farmer_id = len(db_farmers) + 1
    farmer_record = {
        "id": farmer_id,
        "phone": farmer_data.phone,
        "language": farmer_data.language,
        "consent_at": datetime.now().isoformat(),
        "location_lat": farmer_data.location_lat,
        "location_lon": farmer_data.location_lon,
    }
    db_farmers.append(farmer_record)
    
    farm_id = len(db_farms) + 1
    farm_record = {
        "id": farm_id,
        "farmer_id": farmer_id,
        "area_acre": 0, # Placeholder
        "soil_type": "N/A", # Placeholder
        "crop": "Paddy", # Default crop for now
        "created_at": datetime.now().isoformat(),
    }
    db_farms.append(farm_record)

    return {"message": "Farmer and farm created successfully", "farmer_id": farmer_id}