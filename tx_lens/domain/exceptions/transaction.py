from dataclasses import dataclass


@dataclass
class UnexistingTransaction(Exception):
    """Exception raised when a transaction is not found on the blockchain network."""

    tx_hash: str

    def __str__(self) -> str:
        return f"Transaction with hash: '{self.tx_hash}' not found."
