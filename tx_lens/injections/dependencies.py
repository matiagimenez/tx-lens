import inject

from tx_lens.domain.interfaces import NetworkClient
from tx_lens.infrastructure.api_clients.infura import InfuraClient


def configure_injection() -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind_to_provider(NetworkClient, InfuraClient)

    inject.configure(config)
