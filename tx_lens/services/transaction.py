import inject

from tx_lens.domain import NetworkClient, Transaction


class TransactionService:
    @property
    def network_client(self) -> NetworkClient:
        return inject.instance(NetworkClient)  # type: ignore[no-any-return]

    def fetch_transaction(self, tx_hash: str) -> Transaction:
        return self.network_client.get_transaction(tx_hash)

    def explain(self, tx_hash: str) -> Transaction:  # pylint: disable=no-self-use
        tx_data = self.fetch_transaction(tx_hash)
        return tx_data
