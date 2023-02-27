import xmltodict

from boinc_client.clients.rpc_client import RpcClient
from boinc_client.models.old_results import OldResults
from boinc_client.models.result import Results


def results(client: RpcClient, active_only: bool = False) -> dict:
    """Show tasks."""
    rpc_resp = client.make_request(
        f"<get_results><active_only>{int(active_only)}</active_only></get_results>"
    )
    rpc_json = xmltodict.parse(rpc_resp, force_list="result")
    return Results().load(rpc_json)


def old_results(client: RpcClient) -> dict:
    """Show old tasks."""
    rpc_resp = client.make_request("<get_old_results/>")
    rpc_json = xmltodict.parse(rpc_resp, force_list="old_result")
    return OldResults().load(rpc_json)
