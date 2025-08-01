# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.models.providers import (
    anthropic_list_params,
    anthropic_create_params,
    anthropic_update_params,
    anthropic_list_agents_params,
)
from ....types.models.providers.anthropic_list_response import AnthropicListResponse
from ....types.models.providers.anthropic_create_response import AnthropicCreateResponse
from ....types.models.providers.anthropic_delete_response import AnthropicDeleteResponse
from ....types.models.providers.anthropic_update_response import AnthropicUpdateResponse
from ....types.models.providers.anthropic_retrieve_response import AnthropicRetrieveResponse
from ....types.models.providers.anthropic_list_agents_response import AnthropicListAgentsResponse

__all__ = ["AnthropicResource", "AsyncAnthropicResource"]


class AnthropicResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnthropicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AnthropicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnthropicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AnthropicResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        api_key: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnthropicCreateResponse:
        """
        To create an Anthropic API key, send a POST request to
        `/v2/gen-ai/anthropic/keys`.

        Args:
          api_key: Anthropic API key

          name: Name of the key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/gen-ai/anthropic/keys"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/anthropic/keys",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "name": name,
                },
                anthropic_create_params.AnthropicCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnthropicCreateResponse,
        )

    def retrieve(
        self,
        api_key_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnthropicRetrieveResponse:
        """
        To retrieve details of an Anthropic API key, send a GET request to
        `/v2/gen-ai/anthropic/keys/{api_key_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `api_key_uuid` but received {api_key_uuid!r}")
        return self._get(
            f"/v2/gen-ai/anthropic/keys/{api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/anthropic/keys/{api_key_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnthropicRetrieveResponse,
        )

    def update(
        self,
        path_api_key_uuid: str,
        *,
        api_key: str | NotGiven = NOT_GIVEN,
        body_api_key_uuid: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnthropicUpdateResponse:
        """
        To update an Anthropic API key, send a PUT request to
        `/v2/gen-ai/anthropic/keys/{api_key_uuid}`.

        Args:
          api_key: Anthropic API key

          body_api_key_uuid: API key ID

          name: Name of the key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `path_api_key_uuid` but received {path_api_key_uuid!r}")
        return self._put(
            f"/v2/gen-ai/anthropic/keys/{path_api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/anthropic/keys/{path_api_key_uuid}",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "body_api_key_uuid": body_api_key_uuid,
                    "name": name,
                },
                anthropic_update_params.AnthropicUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnthropicUpdateResponse,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnthropicListResponse:
        """
        To list all Anthropic API keys, send a GET request to
        `/v2/gen-ai/anthropic/keys`.

        Args:
          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/gen-ai/anthropic/keys"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/anthropic/keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    anthropic_list_params.AnthropicListParams,
                ),
            ),
            cast_to=AnthropicListResponse,
        )

    def delete(
        self,
        api_key_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnthropicDeleteResponse:
        """
        To delete an Anthropic API key, send a DELETE request to
        `/v2/gen-ai/anthropic/keys/{api_key_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `api_key_uuid` but received {api_key_uuid!r}")
        return self._delete(
            f"/v2/gen-ai/anthropic/keys/{api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/anthropic/keys/{api_key_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnthropicDeleteResponse,
        )

    def list_agents(
        self,
        uuid: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnthropicListAgentsResponse:
        """
        List Agents by Anthropic Key.

        Args:
          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/v2/gen-ai/anthropic/keys/{uuid}/agents"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/anthropic/keys/{uuid}/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    anthropic_list_agents_params.AnthropicListAgentsParams,
                ),
            ),
            cast_to=AnthropicListAgentsResponse,
        )


class AsyncAnthropicResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnthropicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnthropicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnthropicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncAnthropicResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        api_key: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnthropicCreateResponse:
        """
        To create an Anthropic API key, send a POST request to
        `/v2/gen-ai/anthropic/keys`.

        Args:
          api_key: Anthropic API key

          name: Name of the key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/gen-ai/anthropic/keys"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/anthropic/keys",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "name": name,
                },
                anthropic_create_params.AnthropicCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnthropicCreateResponse,
        )

    async def retrieve(
        self,
        api_key_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnthropicRetrieveResponse:
        """
        To retrieve details of an Anthropic API key, send a GET request to
        `/v2/gen-ai/anthropic/keys/{api_key_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `api_key_uuid` but received {api_key_uuid!r}")
        return await self._get(
            f"/v2/gen-ai/anthropic/keys/{api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/anthropic/keys/{api_key_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnthropicRetrieveResponse,
        )

    async def update(
        self,
        path_api_key_uuid: str,
        *,
        api_key: str | NotGiven = NOT_GIVEN,
        body_api_key_uuid: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnthropicUpdateResponse:
        """
        To update an Anthropic API key, send a PUT request to
        `/v2/gen-ai/anthropic/keys/{api_key_uuid}`.

        Args:
          api_key: Anthropic API key

          body_api_key_uuid: API key ID

          name: Name of the key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `path_api_key_uuid` but received {path_api_key_uuid!r}")
        return await self._put(
            f"/v2/gen-ai/anthropic/keys/{path_api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/anthropic/keys/{path_api_key_uuid}",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "body_api_key_uuid": body_api_key_uuid,
                    "name": name,
                },
                anthropic_update_params.AnthropicUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnthropicUpdateResponse,
        )

    async def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnthropicListResponse:
        """
        To list all Anthropic API keys, send a GET request to
        `/v2/gen-ai/anthropic/keys`.

        Args:
          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/gen-ai/anthropic/keys"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/anthropic/keys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    anthropic_list_params.AnthropicListParams,
                ),
            ),
            cast_to=AnthropicListResponse,
        )

    async def delete(
        self,
        api_key_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnthropicDeleteResponse:
        """
        To delete an Anthropic API key, send a DELETE request to
        `/v2/gen-ai/anthropic/keys/{api_key_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `api_key_uuid` but received {api_key_uuid!r}")
        return await self._delete(
            f"/v2/gen-ai/anthropic/keys/{api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/anthropic/keys/{api_key_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnthropicDeleteResponse,
        )

    async def list_agents(
        self,
        uuid: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnthropicListAgentsResponse:
        """
        List Agents by Anthropic Key.

        Args:
          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/v2/gen-ai/anthropic/keys/{uuid}/agents"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/anthropic/keys/{uuid}/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    anthropic_list_agents_params.AnthropicListAgentsParams,
                ),
            ),
            cast_to=AnthropicListAgentsResponse,
        )


class AnthropicResourceWithRawResponse:
    def __init__(self, anthropic: AnthropicResource) -> None:
        self._anthropic = anthropic

        self.create = to_raw_response_wrapper(
            anthropic.create,
        )
        self.retrieve = to_raw_response_wrapper(
            anthropic.retrieve,
        )
        self.update = to_raw_response_wrapper(
            anthropic.update,
        )
        self.list = to_raw_response_wrapper(
            anthropic.list,
        )
        self.delete = to_raw_response_wrapper(
            anthropic.delete,
        )
        self.list_agents = to_raw_response_wrapper(
            anthropic.list_agents,
        )


class AsyncAnthropicResourceWithRawResponse:
    def __init__(self, anthropic: AsyncAnthropicResource) -> None:
        self._anthropic = anthropic

        self.create = async_to_raw_response_wrapper(
            anthropic.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            anthropic.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            anthropic.update,
        )
        self.list = async_to_raw_response_wrapper(
            anthropic.list,
        )
        self.delete = async_to_raw_response_wrapper(
            anthropic.delete,
        )
        self.list_agents = async_to_raw_response_wrapper(
            anthropic.list_agents,
        )


class AnthropicResourceWithStreamingResponse:
    def __init__(self, anthropic: AnthropicResource) -> None:
        self._anthropic = anthropic

        self.create = to_streamed_response_wrapper(
            anthropic.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            anthropic.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            anthropic.update,
        )
        self.list = to_streamed_response_wrapper(
            anthropic.list,
        )
        self.delete = to_streamed_response_wrapper(
            anthropic.delete,
        )
        self.list_agents = to_streamed_response_wrapper(
            anthropic.list_agents,
        )


class AsyncAnthropicResourceWithStreamingResponse:
    def __init__(self, anthropic: AsyncAnthropicResource) -> None:
        self._anthropic = anthropic

        self.create = async_to_streamed_response_wrapper(
            anthropic.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            anthropic.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            anthropic.update,
        )
        self.list = async_to_streamed_response_wrapper(
            anthropic.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            anthropic.delete,
        )
        self.list_agents = async_to_streamed_response_wrapper(
            anthropic.list_agents,
        )
