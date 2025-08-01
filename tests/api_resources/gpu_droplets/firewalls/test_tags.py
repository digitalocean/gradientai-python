# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: Gradient) -> None:
        tag = client.gpu_droplets.firewalls.tags.add(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            tags=["frontend"],
        )
        assert tag is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: Gradient) -> None:
        response = client.gpu_droplets.firewalls.tags.with_raw_response.add(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            tags=["frontend"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert tag is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: Gradient) -> None:
        with client.gpu_droplets.firewalls.tags.with_streaming_response.add(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            tags=["frontend"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_add(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `firewall_id` but received ''"):
            client.gpu_droplets.firewalls.tags.with_raw_response.add(
                firewall_id="",
                tags=["frontend"],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_remove(self, client: Gradient) -> None:
        tag = client.gpu_droplets.firewalls.tags.remove(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            tags=["frontend"],
        )
        assert tag is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_remove(self, client: Gradient) -> None:
        response = client.gpu_droplets.firewalls.tags.with_raw_response.remove(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            tags=["frontend"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert tag is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_remove(self, client: Gradient) -> None:
        with client.gpu_droplets.firewalls.tags.with_streaming_response.remove(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            tags=["frontend"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_remove(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `firewall_id` but received ''"):
            client.gpu_droplets.firewalls.tags.with_raw_response.remove(
                firewall_id="",
                tags=["frontend"],
            )


class TestAsyncTags:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncGradient) -> None:
        tag = await async_client.gpu_droplets.firewalls.tags.add(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            tags=["frontend"],
        )
        assert tag is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.firewalls.tags.with_raw_response.add(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            tags=["frontend"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert tag is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.firewalls.tags.with_streaming_response.add(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            tags=["frontend"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_add(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `firewall_id` but received ''"):
            await async_client.gpu_droplets.firewalls.tags.with_raw_response.add(
                firewall_id="",
                tags=["frontend"],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_remove(self, async_client: AsyncGradient) -> None:
        tag = await async_client.gpu_droplets.firewalls.tags.remove(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            tags=["frontend"],
        )
        assert tag is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.firewalls.tags.with_raw_response.remove(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            tags=["frontend"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert tag is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.firewalls.tags.with_streaming_response.remove(
            firewall_id="bb4b2611-3d72-467b-8602-280330ecd65c",
            tags=["frontend"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `firewall_id` but received ''"):
            await async_client.gpu_droplets.firewalls.tags.with_raw_response.remove(
                firewall_id="",
                tags=["frontend"],
            )
