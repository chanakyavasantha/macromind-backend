# app/models.py - Data models

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class EconomicIndicator(BaseModel):
    series_id: str
    name: str
    latest_value: float
    previous_value: float
    change_percent: float
    date: str
    trend: str  # "up", "down", "stable"

class AgentInsight(BaseModel):
    timestamp: str
    economic_health: str  # "strong", "moderate", "weak"
    key_concerns: List[str]
    opportunities: List[str]
    confidence: float
    summary: str

class AlertMessage(BaseModel):
    severity: str  # "info", "warning", "critical"
    indicator: str
    message: str
    timestamp: str

class HealthCheck(BaseModel):
    status: str
    timestamp: str
    data_available: bool
    last_update: Optional[str] = None