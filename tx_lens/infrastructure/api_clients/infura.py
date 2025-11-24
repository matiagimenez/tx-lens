from web3 import Web3

from tx_lens.domain import NetworkClient, Transaction, TransactionReceipt
from tx_lens.settings import Settings
from tx_lens.utils import logger


class InfuraClient(NetworkClient):
    @property
    def client(self) -> Web3:
        if not Settings.INFURA_API_KEY:
            logger.warning("INFURA_API_KEY is not set. InfuraService will not work.")
            raise ValueError("INFURA_API_KEY is not set")

        url = f"https://mainnet.infura.io/v3/{Settings.INFURA_API_KEY}"
        client = Web3(Web3.HTTPProvider(url))

        if not client.is_connected():
            exception = "Failed to connect to Infura"
            logger.error(exception)
            raise ValueError(exception)

        logger.info("Connected to Infura")
        return client

    def get_transaction(self, tx_hash: str) -> Transaction:
        transaction = self.client.eth.get_transaction(tx_hash)
        return Transaction.model_validate(transaction)

    def get_transaction_receipt(self, tx_hash: str) -> TransactionReceipt:
        transaction_receipt = self.client.eth.get_transaction_receipt(tx_hash)
        return TransactionReceipt.model_validate(transaction_receipt)
