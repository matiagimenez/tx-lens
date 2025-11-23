from fastapi import APIRouter

from .routes import transactions

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(
    transactions.router,
    prefix="/transactions",
    tags=["transactions"],
)
