from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import users, mandi, voice, advisory, pest

app = FastAPI(title="FarmSense API", version="0.1.0")

# CORS for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(mandi.router, prefix="/api", tags=["mandi"])
app.include_router(voice.router, prefix="/api", tags=["voice"])
app.include_router(advisory.router, prefix="/api", tags=["advisory"])
app.include_router(pest.router, prefix="/api", tags=["pest"])

@app.get("/api/health")
async def health_check():
    """A simple health check endpoint."""
    return {"status": "ok"}