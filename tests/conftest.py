from typing import Any

import pytest

from tests.helpers import scrub_infura_api_key
from tx_lens.injections import configure_injections


@pytest.fixture(autouse=True, scope="session")
def _configure_injections() -> None:
    configure_injections()


@pytest.fixture(scope="module")
def vcr_config() -> dict[str, Any]:
    return {
        "filter_headers": ["authorization"],
        "record_mode": "once",
        "before_record_request": scrub_infura_api_key,
    }
