from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from tx_lens.domain import UnexistingTransaction


def handle_unexisting_transaction_exception(
    _: Request,
    exception: UnexistingTransaction,
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": str(exception)},
    )


def register_transactions_exception_handler(app: FastAPI) -> None:
    app.add_exception_handler(
        UnexistingTransaction,
        handle_unexisting_transaction_exception,  # type: ignore[arg-type]
    )


__all__ = ["register_transactions_exception_handler"]
