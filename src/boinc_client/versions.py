import xmltodict

from boinc_client.clients.rpc_client import RpcClient


def client_version(client: RpcClient) -> dict:
    """Used to get the version of the running core client and send the version of the request's source."""
    rpc_resp = client.make_request("<exchange_versions/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return rpc_json["server_version"]


def client_update(client: RpcClient) -> dict:
    """Get newer version number, if any, and download url."""
    rpc_resp = client.make_request("<get_newer_version/>")
    update_root = f"<update>{rpc_resp}</update>"
    rpc_json = xmltodict.parse(update_root)
    return rpc_json
