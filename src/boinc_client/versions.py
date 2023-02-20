import xmltodict

from boinc_client.clients.rpc_client import RpcClient
from boinc_client.models.client_update import ClientUpdate
from boinc_client.models.client_version import ClientVersion


def client_version(client: RpcClient) -> dict:
    """Used to get the version of the running core client and send the version of the request's source."""
    rpc_resp = client.make_request("<exchange_versions/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return ClientVersion().load(rpc_json)


def client_update(client: RpcClient) -> dict:
    """Get newer version number, if any, and download url."""
    rpc_resp = client.make_request("<get_newer_version/>")
    update_root = f"<update>{rpc_resp}</update>"
    rpc_json = xmltodict.parse(update_root)
    return ClientUpdate().load(rpc_json)
