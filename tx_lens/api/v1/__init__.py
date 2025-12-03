from fastapi import APIRouter, FastAPI

from .routes import register_transactions_exception_handler, transactions

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(
    transactions.router,
    prefix="/transactions",
    tags=["transactions"],
)


def register_v1_exception_handlers(app: FastAPI) -> None:
    register_transactions_exception_handler(app)


__all__ = ["v1_router", "register_v1_exception_handlers"]
