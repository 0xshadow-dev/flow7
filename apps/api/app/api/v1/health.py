from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "flow7-api"
    }

@router.get("/health/db")
async def database_health():
    """Database health check - placeholder for now"""
    return {
        "status": "not_implemented",
        "message": "Database health check coming soon"
    }