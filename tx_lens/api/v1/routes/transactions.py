from typing import Annotated

from fastapi import APIRouter, Depends
from loguru import logger

from tx_lens.domain import Transaction
from tx_lens.services import TransactionService

from .schemas import TransactionRequest, TransactionResponse

router = APIRouter()

TransactionServiceDependency = Annotated[
    TransactionService,
    Depends(TransactionService),
]


@router.post("/explain")
async def explain_transaction(
    request: TransactionRequest, service: TransactionServiceDependency
) -> TransactionResponse:
    """
    Convert a raw blockchain transaction into a human-readable explanation.
    """
    logger.info(f"Processing transaction: {request.hash_}")

    tx = service.explain(Transaction(hash=request.hash_))

    return TransactionResponse(
        hash=tx.hash_,
        explanation="Transaction explanation will be implemented here",
        blockchain=request.blockchain,
    )
