# api/insights.py - AI insights endpoints

from fastapi import APIRouter, HTTPException
from typing import List

from app.models import AgentInsight, AlertMessage
from app.agent import intelligence_agent
from app.data_fetcher import get_economic_data

router = APIRouter()

@router.get("/insights", response_model=AgentInsight)
async def get_insights():
    """Get AI-generated economic insights"""
    data = get_economic_data()
    if not data:
        raise HTTPException(status_code=503, detail="Data not available")
    
    insights = intelligence_agent.analyze_economic_conditions(data)
    return insights

@router.get("/alerts", response_model=List[AlertMessage])
async def get_alerts():
    """Get current economic alerts"""
    data = get_economic_data()
    if not data:
        return []
    
    alerts = intelligence_agent.check_alerts(data)
    return alerts