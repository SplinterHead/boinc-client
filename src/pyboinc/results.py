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
    rpc_json = xmltodict.parse(rpc_resp)
    result = rpc_json["results"]["result"]
    if type(result) == dict:
        result = [result]
    results = {"results": []}
    for r in result:
        results["results"].append(r)
    return results


def old_results(client: RpcClient) -> dict:
    rpc_resp = client.make_request("<get_old_results/>")
    rpc_json = xmltodict.parse(rpc_resp)
    old_result = rpc_json["old_results"]["old_result"]
    if type(old_result) is dict:
        old_result = [old_result]
    return {"old_results": [result for result in old_result]}
