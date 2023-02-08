import xmltodict

from pyboinc.clients.rpc_client import RpcClient


def cc_status(client: RpcClient) -> dict:
    """Show CPU/GPU/network run modes and network connection status."""
    rpc_resp = client.make_request("<get_cc_status/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return rpc_json


def disk_stats(client: RpcClient) -> dict:
    """Show disk usage by project."""
    rpc_resp = client.make_request("<get_disk_usage/>")
    rpc_json = xmltodict.parse(rpc_resp, force_list="project")
    disk_stats = {"disk_stats": rpc_json.get("disk_usage_summary")}
    if "project" in rpc_json.get("disk_usage_summary"):
        disk_stats["disk_stats"]["projects"] = [
            project for project in rpc_json["disk_usage_summary"]["project"]
        ]
        del disk_stats["disk_stats"]["project"]
    else:
        disk_stats["disk_stats"]["projects"] = []
    return disk_stats


def file_transfers(client: RpcClient) -> dict:
    """Show all current file transfers."""
    rpc_resp = client.make_request("<get_file_transfers/>")
    rpc_json = xmltodict.parse(rpc_resp, force_list=("file_transfer",))
    file_transfers = {"file_transfers": []}
    for transfer in rpc_json['file_transfers']['file_transfer']:
        file_transfers['file_transfers'].append(transfer)
    return file_transfers
