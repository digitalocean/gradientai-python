# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OpenAICreateParams"]


class OpenAICreateParams(TypedDict, total=False):
    api_key: str
    """OpenAI API key"""

    name: str
    """Name of the key"""
