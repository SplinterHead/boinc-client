import xmltodict

from pyboinc.clients.rpc_client import RpcClient


def results(client: RpcClient) -> dict:
    """Show tasks."""
    rpc_resp = client.make_request("<get_results/>")
    rpc_json = xmltodict.parse(rpc_resp)
    result = rpc_json["results"]["result"]
    if type(result) == dict:
        result = [result]
    results = {"results": []}
    for r in result:
        results["results"].append(r)
    return results
