import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv(Path(__file__).resolve().parents[1] / '.env')

from app.admin.routes import router as admin_router
from app.auth.routes import router as auth_router
from app.projects.routes import router as projects_router
from app.leads.routes import router as leads_router
from app.services.routes import router as services_router
from app.world.routes import router as world_router

app = FastAPI(title="Hengshi Design API")

cors_origins = [
    origin.strip()
    for origin in os.getenv(
        'CORS_ORIGINS',
        'http://localhost:5173,http://127.0.0.1:5173'
    ).split(',')
    if origin.strip()
]

cors_origin_regex = os.getenv('CORS_ORIGIN_REGEX', '').strip() or None

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_origin_regex=cors_origin_regex,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(admin_router, prefix="/api/admin", tags=["admin"])
app.include_router(services_router, prefix="/api", tags=["services"])
app.include_router(projects_router, prefix="/api", tags=["projects"])
app.include_router(leads_router, prefix="/api", tags=["leads"])
app.include_router(world_router, prefix="/api", tags=["world"])


@app.get("/health")
async def health_check() -> dict:
    return {"status": "ok"}
