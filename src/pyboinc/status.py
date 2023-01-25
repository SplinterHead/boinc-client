import xmltodict

from pyboinc.clients.rpc_client import RpcClient


def cc_status(client: RpcClient):
    """Show CPU/GPU/network run modes and network connection status."""
    rpc_resp = client.make_request("<get_cc_status/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return rpc_json
