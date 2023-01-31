import xmltodict

from pyboinc.clients.rpc_client import RpcClient


def client_version(client: RpcClient) -> dict:
    """Used to get the version of the running core client and send the version of the request's source."""
    rpc_resp = client.make_request("<exchange_versions/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return rpc_json["server_version"]
