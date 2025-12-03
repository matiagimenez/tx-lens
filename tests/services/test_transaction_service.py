import pytest

from tx_lens.domain import Transaction, UnexistingTransaction
from tx_lens.services import TransactionService


@pytest.mark.vcr
def test_fetch_transaction(
    transaction_service: TransactionService,
    transaction_hash: str,
) -> None:
    tx = transaction_service.fetch_transaction(transaction_hash)
    assert isinstance(tx, Transaction)


@pytest.mark.vcr
def test_fetch_unexisting_transaction(
    transaction_service: TransactionService,
    unexisting_transaction_hash: str,
) -> None:
    with pytest.raises(UnexistingTransaction):
        transaction_service.fetch_transaction(unexisting_transaction_hash)
