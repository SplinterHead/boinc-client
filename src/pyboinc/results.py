import xmltodict

from pyboinc.clients.rpc_client import RpcClient


def results(client: RpcClient, active_only: bool = False) -> dict:
    """Show tasks."""
    if active_only:
        rpc_resp = client.make_request(
            "<get_results><active_only></active_only></get_results>"
        )
    else:
        rpc_resp = client.make_request("<get_results/>")
    rpc_json = xmltodict.parse(rpc_resp, force_list="result")
    return {"results": [r for r in rpc_json["results"]["result"]]}


def old_results(client: RpcClient) -> dict:
    """Show old tasks."""
    rpc_resp = client.make_request("<get_old_results/>")
    rpc_json = xmltodict.parse(rpc_resp, force_list="old_result")
    return {"old_results": [r for r in rpc_json["old_results"]["old_result"]]}
