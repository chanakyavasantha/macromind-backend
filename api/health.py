# api/health.py - Health check endpoints

from fastapi import APIRouter
from datetime import datetime

from app.models import HealthCheck
from app.data_fetcher import get_economic_data

router = APIRouter()

@router.get("/health", response_model=HealthCheck)
async def health_check():
    """API health check"""
    data = get_economic_data()
    
    return HealthCheck(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        data_available=len(data) > 0,
        last_update=datetime.now().isoformat() if data else None
    )