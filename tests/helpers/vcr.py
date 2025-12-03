import re
from typing import Any


def scrub_infura_api_key(request: Any) -> Any:
    """Replace Infura API keys in the request URI."""
    if hasattr(request, "uri") and "infura.io" in request.uri:
        request.uri = re.sub(r"/v3/[^/]+", "/v3/[REDACTED]", request.uri)
    return request
