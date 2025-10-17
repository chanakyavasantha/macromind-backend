# api/indicators.py - Economic indicators endpoints

from fastapi import APIRouter, HTTPException
from typing import Dict

from app.models import EconomicIndicator
from app.data_fetcher import get_economic_data

router = APIRouter()

@router.get("/indicators", response_model=Dict[str, EconomicIndicator])
async def get_indicators():
    """Get all economic indicators"""
    data = get_economic_data()
    if not data:
        raise HTTPException(status_code=503, detail="Data not available")
    return data

@router.get("/indicators/{indicator_name}", response_model=EconomicIndicator)
async def get_indicator(indicator_name: str):
    """Get specific economic indicator"""
    data = get_economic_data()
    indicator_name = indicator_name.upper()
    
    if indicator_name not in data:
        raise HTTPException(status_code=404, detail=f"Indicator {indicator_name} not found")
    
    return data[indicator_name]