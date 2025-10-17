# app/config.py - Configuration settings

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    def __init__(self):
        # API Configuration
        self.FRED_API_KEY = os.getenv("FRED_API_KEY", "")
        self.API_HOST = os.getenv("API_HOST", "0.0.0.0")
        self.API_PORT = int(os.getenv("API_PORT", "8000"))
        self.DEBUG = os.getenv("DEBUG", "false").lower() == "true"
        
        # Optional settings
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
        
        # Validate required settings
        if not self.FRED_API_KEY:
            raise ValueError("FRED_API_KEY is required. Please set it in your .env file")

settings = Settings()

# FRED API Configuration
BASE_FRED_URL = "https://api.stlouisfed.org/fred"

# Core Economic Indicators
CORE_INDICATORS = {
    "GDP": {"series_id": "GDP", "name": "Gross Domestic Product"},
    "UNEMPLOYMENT": {"series_id": "UNRATE", "name": "Unemployment Rate"},
    "INFLATION": {"series_id": "CPIAUCSL", "name": "Consumer Price Index"},
    "FED_FUNDS": {"series_id": "FEDFUNDS", "name": "Federal Funds Rate"},
    "CONSUMER_SENTIMENT": {"series_id": "UMCSENT", "name": "Consumer Sentiment"}
}