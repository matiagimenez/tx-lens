from fastapi import APIRouter
from loguru import logger

from tx_lens.schemas.transaction import TransactionRequest, TransactionResponse

router = APIRouter()


@router.post("/explain", response_model=TransactionResponse)
async def explain_transaction(request: TransactionRequest):
    """
    Convert a raw blockchain transaction into a human-readable explanation.
    """
    logger.info(f"Processing transaction: {request.transaction_hash}")

    return TransactionResponse(
        transaction_hash=request.transaction_hash,
        explanation="Transaction explanation will be implemented here",
        blockchain=request.blockchain,
    )


@router.get("/{transaction_hash}", response_model=TransactionResponse)
async def get_transaction(transaction_hash: str, blockchain: str = "ethereum"):
    """
    Get explanation for a specific transaction.
    """
    logger.info(f"Fetching transaction: {transaction_hash}")

    return TransactionResponse(
        transaction_hash=transaction_hash,
        explanation="Transaction explanation will be implemented here",
        blockchain=blockchain,
    )
