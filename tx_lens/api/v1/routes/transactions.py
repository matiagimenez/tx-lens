from fastapi import APIRouter
from loguru import logger

from .schemas import TransactionRequest, TransactionResponse

router = APIRouter()


@router.post("/explain")
async def explain_transaction(request: TransactionRequest) -> TransactionResponse:
    """
    Convert a raw blockchain transaction into a human-readable explanation.
    """
    logger.info(f"Processing transaction: {request.transaction_hash}")

    return TransactionResponse(
        transaction_hash=request.transaction_hash,
        explanation="Transaction explanation will be implemented here",
        blockchain=request.blockchain,
    )
