import inject

from .injections import _configure_injections


def configure_injections() -> None:
    inject.clear_and_configure(_configure_injections)


__all__ = ["configure_injections"]
