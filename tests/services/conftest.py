import pytest

from tx_lens.services import TransactionService


@pytest.fixture
def transaction_hash() -> str:
    return "0x206d9ed0458f07377c05045b1c9d3e4cdb03c03141f4070f5f88dd512d74dda0"


@pytest.fixture
def unexisting_transaction_hash() -> str:
    return "0x0000000000000000000000000000000000000000000000000000000000000000"


@pytest.fixture
def transaction_service() -> TransactionService:
    return TransactionService()
