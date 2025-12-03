import inject

from tx_lens.domain.interfaces import NetworkClient
from tx_lens.infrastructure.api_clients.infura import InfuraClient


def _configure_injections(binder: inject.Binder) -> None:
    binder.bind_to_provider(NetworkClient, InfuraClient)
