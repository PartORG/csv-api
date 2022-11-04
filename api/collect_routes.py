"""
File collects together all written API Routes.
"""
from fastapi import APIRouter

# inport every created route
from api.v1 import route_information
from api.v1 import route_production

# collect all API Routes together
api_router = APIRouter()
api_router.include_router(route_information.router, prefix="/info", tags=["information"])
api_router.include_router(route_production.router, prefix="/prod", tags=["production"])
