"""Command to purge downloads."""

from aria2p.api import API


def purge(api: API) -> int:
    """
    Purge subcommand.

    Arguments:
        api: The API instance to use.

    Returns:
        int: 0 if all success, 1 if one failure.
    """
    return 0 if api.autopurge() else 1
