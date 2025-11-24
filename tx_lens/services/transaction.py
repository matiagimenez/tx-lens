import inject

from tx_lens.domain import NetworkClient, Transaction


class TransactionService:
    @property
    def network_client(self) -> NetworkClient:
        return inject.instance(NetworkClient)  # type: ignore[no-any-return]

    def explain(self, tx_hash: str) -> Transaction:  # pylint: disable=no-self-use
        return self.network_client.get_transaction(tx_hash)
