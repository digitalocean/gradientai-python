# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["IndexingJobCreateParams"]


class IndexingJobCreateParams(TypedDict, total=False):
    data_source_uuids: List[str]
    """
    List of data source ids to index, if none are provided, all data sources will be
    indexed
    """

    knowledge_base_uuid: str
    """Knowledge base id"""
