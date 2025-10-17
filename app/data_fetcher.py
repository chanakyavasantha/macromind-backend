# app/data_fetcher.py - FRED API data fetching

import httpx
from typing import Dict, Optional
from datetime import datetime

from .config import settings, BASE_FRED_URL, CORE_INDICATORS
from .models import EconomicIndicator

# Global cache
economic_data_cache: Dict[str, EconomicIndicator] = {}

class FREDDataFetcher:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = BASE_FRED_URL
    
    async def fetch_latest_data(self, series_id: str, limit: int = 10) -> Optional[Dict]:
        """Fetch latest data for a specific series"""
        async with httpx.AsyncClient() as client:
            try:
                url = f"{self.base_url}/series/observations"
                params = {
                    "series_id": series_id,
                    "api_key": self.api_key,
                    "file_type": "json",
                    "limit": limit,
                    "sort_order": "desc"
                }
                
                response = await client.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                
                if "observations" in data and len(data["observations"]) >= 2:
                    latest = data["observations"][0]
                    previous = data["observations"][1]
                    
                    latest_val = float(latest["value"]) if latest["value"] != "." else 0
                    prev_val = float(previous["value"]) if previous["value"] != "." else 0
                    
                    change_percent = ((latest_val - prev_val) / prev_val * 100) if prev_val != 0 else 0
                    
                    return {
                        "series_id": series_id,
                        "latest_value": latest_val,
                        "previous_value": prev_val,
                        "change_percent": round(change_percent, 2),
                        "date": latest["date"],
                        "trend": "up" if change_percent > 0.1 else "down" if change_percent < -0.1 else "stable"
                    }
                
                return None
                
            except Exception as e:
                print(f"Error fetching {series_id}: {e}")
                return None

# Initialize fetcher
data_fetcher = FREDDataFetcher(settings.FRED_API_KEY)

async def update_economic_data():
    """Update global economic data cache"""
    global economic_data_cache
    
    indicators = {}
    
    for key, config in CORE_INDICATORS.items():
        data = await data_fetcher.fetch_latest_data(config["series_id"])
        if data:
            indicators[key] = EconomicIndicator(
                series_id=data["series_id"],
                name=config["name"],
                latest_value=data["latest_value"],
                previous_value=data["previous_value"],
                change_percent=data["change_percent"],
                date=data["date"],
                trend=data["trend"]
            )
    
    economic_data_cache = indicators
    print(f"Updated economic data at {datetime.now()}")

def get_economic_data() -> Dict[str, EconomicIndicator]:
    """Get current economic data"""
    return economic_data_cache