from fastapi import APIRouter

from tx_lens.api.v1.endpoints import transactions

v1_router = APIRouter()

v1_router.include_router(
    transactions.router,
    prefix="/transactions",
    tags=["transactions"],
)
