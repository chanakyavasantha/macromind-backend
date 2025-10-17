# main.py - Application entry point

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import asyncio

from app.config import settings
from api.indicators import router as indicators_router
from api.insights import router as insights_router
from api.health import router as health_router
from app.data_fetcher import update_economic_data

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Fetch initial data
    await update_economic_data()
    
    # Schedule periodic updates
    asyncio.create_task(periodic_update())
    
    yield

async def periodic_update():
    """Update data every hour"""
    while True:
        await asyncio.sleep(3600)
        await update_economic_data()

# Create FastAPI app
app = FastAPI(
    title="MacroMind API",
    description="Real-time macroeconomic analytics with AI insights",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(indicators_router, prefix="/api")
app.include_router(insights_router, prefix="/api")
app.include_router(health_router, prefix="/api")

@app.get("/")
async def root():
    return {
        "message": "MacroMind API",
        "version": "1.0.0",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG
    )