# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import TypedDict

__all__ = ["FirewallRuleTarget"]


class FirewallRuleTarget(TypedDict, total=False):
    addresses: List[str]
    """
    An array of strings containing the IPv4 addresses, IPv6 addresses, IPv4 CIDRs,
    and/or IPv6 CIDRs to which the firewall will allow traffic.
    """

    droplet_ids: Iterable[int]
    """
    An array containing the IDs of the Droplets to which the firewall will allow
    traffic.
    """

    kubernetes_ids: List[str]
    """
    An array containing the IDs of the Kubernetes clusters to which the firewall
    will allow traffic.
    """

    load_balancer_uids: List[str]
    """
    An array containing the IDs of the load balancers to which the firewall will
    allow traffic.
    """

    tags: Optional[List[str]]
    """A flat array of tag names as strings to be applied to the resource.

    Tag names must exist in order to be referenced in a request.

    Requires `tag:create` and `tag:read` scopes.
    """
