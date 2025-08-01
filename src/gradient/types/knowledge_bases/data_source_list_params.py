# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DataSourceListParams"]


class DataSourceListParams(TypedDict, total=False):
    page: int
    """Page number."""

    per_page: int
    """Items per page."""
