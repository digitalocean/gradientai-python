# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.agents.evaluation_metrics.openai import (
    key_list_params,
    key_create_params,
    key_update_params,
    key_list_agents_params,
)
from .....types.agents.evaluation_metrics.openai.key_list_response import KeyListResponse
from .....types.agents.evaluation_metrics.openai.key_create_response import KeyCreateResponse
from .....types.agents.evaluation_metrics.openai.key_delete_response import KeyDeleteResponse
from .....types.agents.evaluation_metrics.openai.key_update_response import KeyUpdateResponse
from .....types.agents.evaluation_metrics.openai.key_retrieve_response import KeyRetrieveResponse
from .....types.agents.evaluation_metrics.openai.key_list_agents_response import KeyListAgentsResponse

__all__ = ["KeysResource", "AsyncKeysResource"]


class KeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return KeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return KeysResourceWithStreamingResponse(self)

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
    ) -> KeyCreateResponse:
        """
        To create an OpenAI API key, send a POST request to `/v2/gen-ai/openai/keys`.

        Args:
          api_key: OpenAI API key

          name: Name of the key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/gen-ai/openai/keys"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/openai/keys",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "name": name,
                },
                key_create_params.KeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyCreateResponse,
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
    ) -> KeyRetrieveResponse:
        """
        To retrieve details of an OpenAI API key, send a GET request to
        `/v2/gen-ai/openai/keys/{api_key_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `api_key_uuid` but received {api_key_uuid!r}")
        return self._get(
            f"/v2/gen-ai/openai/keys/{api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/openai/keys/{api_key_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyRetrieveResponse,
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
    ) -> KeyUpdateResponse:
        """
        To update an OpenAI API key, send a PUT request to
        `/v2/gen-ai/openai/keys/{api_key_uuid}`.

        Args:
          api_key: OpenAI API key

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
            f"/v2/gen-ai/openai/keys/{path_api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/openai/keys/{path_api_key_uuid}",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "body_api_key_uuid": body_api_key_uuid,
                    "name": name,
                },
                key_update_params.KeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyUpdateResponse,
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
    ) -> KeyListResponse:
        """
        To list all OpenAI API keys, send a GET request to `/v2/gen-ai/openai/keys`.

        Args:
          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/gen-ai/openai/keys"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/openai/keys",
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
                    key_list_params.KeyListParams,
                ),
            ),
            cast_to=KeyListResponse,
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
    ) -> KeyDeleteResponse:
        """
        To delete an OpenAI API key, send a DELETE request to
        `/v2/gen-ai/openai/keys/{api_key_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `api_key_uuid` but received {api_key_uuid!r}")
        return self._delete(
            f"/v2/gen-ai/openai/keys/{api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/openai/keys/{api_key_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyDeleteResponse,
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
    ) -> KeyListAgentsResponse:
        """
        List Agents by OpenAI Key.

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
            f"/v2/gen-ai/openai/keys/{uuid}/agents"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/openai/keys/{uuid}/agents",
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
                    key_list_agents_params.KeyListAgentsParams,
                ),
            ),
            cast_to=KeyListAgentsResponse,
        )


class AsyncKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/gradient-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/gradient-python#with_streaming_response
        """
        return AsyncKeysResourceWithStreamingResponse(self)

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
    ) -> KeyCreateResponse:
        """
        To create an OpenAI API key, send a POST request to `/v2/gen-ai/openai/keys`.

        Args:
          api_key: OpenAI API key

          name: Name of the key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/gen-ai/openai/keys"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/openai/keys",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "name": name,
                },
                key_create_params.KeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyCreateResponse,
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
    ) -> KeyRetrieveResponse:
        """
        To retrieve details of an OpenAI API key, send a GET request to
        `/v2/gen-ai/openai/keys/{api_key_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `api_key_uuid` but received {api_key_uuid!r}")
        return await self._get(
            f"/v2/gen-ai/openai/keys/{api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/openai/keys/{api_key_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyRetrieveResponse,
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
    ) -> KeyUpdateResponse:
        """
        To update an OpenAI API key, send a PUT request to
        `/v2/gen-ai/openai/keys/{api_key_uuid}`.

        Args:
          api_key: OpenAI API key

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
            f"/v2/gen-ai/openai/keys/{path_api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/openai/keys/{path_api_key_uuid}",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "body_api_key_uuid": body_api_key_uuid,
                    "name": name,
                },
                key_update_params.KeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyUpdateResponse,
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
    ) -> KeyListResponse:
        """
        To list all OpenAI API keys, send a GET request to `/v2/gen-ai/openai/keys`.

        Args:
          page: Page number.

          per_page: Items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/gen-ai/openai/keys"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/openai/keys",
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
                    key_list_params.KeyListParams,
                ),
            ),
            cast_to=KeyListResponse,
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
    ) -> KeyDeleteResponse:
        """
        To delete an OpenAI API key, send a DELETE request to
        `/v2/gen-ai/openai/keys/{api_key_uuid}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_uuid:
            raise ValueError(f"Expected a non-empty value for `api_key_uuid` but received {api_key_uuid!r}")
        return await self._delete(
            f"/v2/gen-ai/openai/keys/{api_key_uuid}"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/openai/keys/{api_key_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyDeleteResponse,
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
    ) -> KeyListAgentsResponse:
        """
        List Agents by OpenAI Key.

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
            f"/v2/gen-ai/openai/keys/{uuid}/agents"
            if self._client._base_url_overridden
            else f"https://api.digitalocean.com/v2/gen-ai/openai/keys/{uuid}/agents",
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
                    key_list_agents_params.KeyListAgentsParams,
                ),
            ),
            cast_to=KeyListAgentsResponse,
        )


class KeysResourceWithRawResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.create = to_raw_response_wrapper(
            keys.create,
        )
        self.retrieve = to_raw_response_wrapper(
            keys.retrieve,
        )
        self.update = to_raw_response_wrapper(
            keys.update,
        )
        self.list = to_raw_response_wrapper(
            keys.list,
        )
        self.delete = to_raw_response_wrapper(
            keys.delete,
        )
        self.list_agents = to_raw_response_wrapper(
            keys.list_agents,
        )


class AsyncKeysResourceWithRawResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.create = async_to_raw_response_wrapper(
            keys.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            keys.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            keys.update,
        )
        self.list = async_to_raw_response_wrapper(
            keys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            keys.delete,
        )
        self.list_agents = async_to_raw_response_wrapper(
            keys.list_agents,
        )


class KeysResourceWithStreamingResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.create = to_streamed_response_wrapper(
            keys.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            keys.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            keys.update,
        )
        self.list = to_streamed_response_wrapper(
            keys.list,
        )
        self.delete = to_streamed_response_wrapper(
            keys.delete,
        )
        self.list_agents = to_streamed_response_wrapper(
            keys.list_agents,
        )


class AsyncKeysResourceWithStreamingResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.create = async_to_streamed_response_wrapper(
            keys.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            keys.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            keys.update,
        )
        self.list = async_to_streamed_response_wrapper(
            keys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            keys.delete,
        )
        self.list_agents = async_to_streamed_response_wrapper(
            keys.list_agents,
        )
