from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import uuid
from datetime import datetime, timedelta

router = APIRouter()

# In-memory storage for MVP. Use a real database in production.
review_queue = []

class PestReport(BaseModel):
    ticket_id: str
    image_url: str
    status: str
    created_at: str
    expected_sla: str

@router.post("/pest/submit")
async def submit_pest_report(file: UploadFile = File(...)):
    """
    Accepts an image upload for pest identification.
    In the MVP, this acts as a placeholder and puts the image in a review queue.
    """
    # In a real application, you would:
    # 1. Save the image to a storage service (e.g., AWS S3, local disk).
    # 2. Add an entry to the database.
    # 3. Trigger a background job for AI model inference and/or human review.
    
    # For this MVP, we will simulate the process.
    file_id = str(uuid.uuid4())
    # Mock a file save, but don't actually save it.
    # file_path = f"/path/to/pest_images/{file_id}.jpg" 
    
    ticket_id = f"PEST-{file_id[:8]}"
    
    report = {
        "ticket_id": ticket_id,
        "image_url": f"/static/pest_images/{file_id}.jpg", # Mock URL
        "status": "pending_review",
        "created_at": datetime.now().isoformat(),
        "expected_sla": (datetime.now() + timedelta(hours=24)).isoformat()
    }
    
    review_queue.append(report)
    
    return {
        "message": "Image submitted successfully. It has been queued for review.",
        "ticket_id": report["ticket_id"],
        "sla": "24 hours"
    }