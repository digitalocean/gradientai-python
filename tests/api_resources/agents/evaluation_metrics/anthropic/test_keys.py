# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.agents.evaluation_metrics.anthropic import (
    KeyListResponse,
    KeyCreateResponse,
    KeyDeleteResponse,
    KeyUpdateResponse,
    KeyRetrieveResponse,
    KeyListAgentsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Gradient) -> None:
        key = client.agents.evaluation_metrics.anthropic.keys.create()
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Gradient) -> None:
        key = client.agents.evaluation_metrics.anthropic.keys.create(
            api_key='"sk-ant-12345678901234567890123456789012"',
            name='"Production Key"',
        )
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.anthropic.keys.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.anthropic.keys.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyCreateResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        key = client.agents.evaluation_metrics.anthropic.keys.retrieve(
            "api_key_uuid",
        )
        assert_matches_type(KeyRetrieveResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.anthropic.keys.with_raw_response.retrieve(
            "api_key_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyRetrieveResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.anthropic.keys.with_streaming_response.retrieve(
            "api_key_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyRetrieveResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_uuid` but received ''"):
            client.agents.evaluation_metrics.anthropic.keys.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Gradient) -> None:
        key = client.agents.evaluation_metrics.anthropic.keys.update(
            path_api_key_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(KeyUpdateResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Gradient) -> None:
        key = client.agents.evaluation_metrics.anthropic.keys.update(
            path_api_key_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            api_key='"sk-ant-12345678901234567890123456789012"',
            body_api_key_uuid='"12345678-1234-1234-1234-123456789012"',
            name='"Production Key"',
        )
        assert_matches_type(KeyUpdateResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.anthropic.keys.with_raw_response.update(
            path_api_key_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyUpdateResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.anthropic.keys.with_streaming_response.update(
            path_api_key_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyUpdateResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_api_key_uuid` but received ''"):
            client.agents.evaluation_metrics.anthropic.keys.with_raw_response.update(
                path_api_key_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        key = client.agents.evaluation_metrics.anthropic.keys.list()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Gradient) -> None:
        key = client.agents.evaluation_metrics.anthropic.keys.list(
            page=0,
            per_page=0,
        )
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.anthropic.keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.anthropic.keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyListResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Gradient) -> None:
        key = client.agents.evaluation_metrics.anthropic.keys.delete(
            "api_key_uuid",
        )
        assert_matches_type(KeyDeleteResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.anthropic.keys.with_raw_response.delete(
            "api_key_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyDeleteResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.anthropic.keys.with_streaming_response.delete(
            "api_key_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyDeleteResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_uuid` but received ''"):
            client.agents.evaluation_metrics.anthropic.keys.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_agents(self, client: Gradient) -> None:
        key = client.agents.evaluation_metrics.anthropic.keys.list_agents(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(KeyListAgentsResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_agents_with_all_params(self, client: Gradient) -> None:
        key = client.agents.evaluation_metrics.anthropic.keys.list_agents(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
            page=0,
            per_page=0,
        )
        assert_matches_type(KeyListAgentsResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_agents(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.anthropic.keys.with_raw_response.list_agents(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyListAgentsResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_agents(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.anthropic.keys.with_streaming_response.list_agents(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyListAgentsResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_agents(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.agents.evaluation_metrics.anthropic.keys.with_raw_response.list_agents(
                uuid="",
            )


class TestAsyncKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncGradient) -> None:
        key = await async_client.agents.evaluation_metrics.anthropic.keys.create()
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradient) -> None:
        key = await async_client.agents.evaluation_metrics.anthropic.keys.create(
            api_key='"sk-ant-12345678901234567890123456789012"',
            name='"Production Key"',
        )
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.anthropic.keys.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_metrics.anthropic.keys.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyCreateResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        key = await async_client.agents.evaluation_metrics.anthropic.keys.retrieve(
            "api_key_uuid",
        )
        assert_matches_type(KeyRetrieveResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.anthropic.keys.with_raw_response.retrieve(
            "api_key_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyRetrieveResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_metrics.anthropic.keys.with_streaming_response.retrieve(
            "api_key_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyRetrieveResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_uuid` but received ''"):
            await async_client.agents.evaluation_metrics.anthropic.keys.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncGradient) -> None:
        key = await async_client.agents.evaluation_metrics.anthropic.keys.update(
            path_api_key_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(KeyUpdateResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGradient) -> None:
        key = await async_client.agents.evaluation_metrics.anthropic.keys.update(
            path_api_key_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            api_key='"sk-ant-12345678901234567890123456789012"',
            body_api_key_uuid='"12345678-1234-1234-1234-123456789012"',
            name='"Production Key"',
        )
        assert_matches_type(KeyUpdateResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.anthropic.keys.with_raw_response.update(
            path_api_key_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyUpdateResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_metrics.anthropic.keys.with_streaming_response.update(
            path_api_key_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyUpdateResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_api_key_uuid` but received ''"):
            await async_client.agents.evaluation_metrics.anthropic.keys.with_raw_response.update(
                path_api_key_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        key = await async_client.agents.evaluation_metrics.anthropic.keys.list()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradient) -> None:
        key = await async_client.agents.evaluation_metrics.anthropic.keys.list(
            page=0,
            per_page=0,
        )
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.anthropic.keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_metrics.anthropic.keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyListResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradient) -> None:
        key = await async_client.agents.evaluation_metrics.anthropic.keys.delete(
            "api_key_uuid",
        )
        assert_matches_type(KeyDeleteResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.anthropic.keys.with_raw_response.delete(
            "api_key_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyDeleteResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_metrics.anthropic.keys.with_streaming_response.delete(
            "api_key_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyDeleteResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_uuid` but received ''"):
            await async_client.agents.evaluation_metrics.anthropic.keys.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_agents(self, async_client: AsyncGradient) -> None:
        key = await async_client.agents.evaluation_metrics.anthropic.keys.list_agents(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(KeyListAgentsResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_agents_with_all_params(self, async_client: AsyncGradient) -> None:
        key = await async_client.agents.evaluation_metrics.anthropic.keys.list_agents(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
            page=0,
            per_page=0,
        )
        assert_matches_type(KeyListAgentsResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_agents(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.anthropic.keys.with_raw_response.list_agents(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyListAgentsResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_agents(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_metrics.anthropic.keys.with_streaming_response.list_agents(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyListAgentsResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_agents(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.agents.evaluation_metrics.anthropic.keys.with_raw_response.list_agents(
                uuid="",
            )
