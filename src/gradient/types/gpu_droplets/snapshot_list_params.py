# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SnapshotListParams"]


class SnapshotListParams(TypedDict, total=False):
    page: int
    """Which 'page' of paginated results to return."""

    per_page: int
    """Number of items returned per page"""

    resource_type: Literal["droplet", "volume"]
    """Used to filter snapshots by a resource type."""
