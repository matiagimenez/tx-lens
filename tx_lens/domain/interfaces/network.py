from abc import ABC, abstractmethod

from tx_lens.domain.models import Transaction, TransactionReceipt


class NetworkClient(ABC):
    @abstractmethod
    def get_transaction(self, tx_hash: str) -> Transaction: ...

    @abstractmethod
    def get_transaction_receipt(self, tx_hash: str) -> TransactionReceipt: ...
