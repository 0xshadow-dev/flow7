from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.health import router as health_router

# Create FastAPI app
app = FastAPI(
    title="Flow7 API",
    description="AI Agent Platform API",
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# Configure CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health_router, prefix="/api/v1", tags=["health"])

@app.get("/")
async def root():
    return {"message": "Flow7 API is running"}
