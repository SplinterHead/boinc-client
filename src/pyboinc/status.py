import xmltodict

from pyboinc.clients.rpc_client import RpcClient


def cc_status(client: RpcClient):
    """Show CPU/GPU/network run modes and network connection status."""
    rpc_resp = client.make_request("<get_cc_status/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return rpc_json


def disk_stats(client: RpcClient):
    """Show disk usage by project."""
    rpc_resp = client.make_request("<get_disk_usage/>")
    rpc_json = xmltodict.parse(rpc_resp)
    disk_stats = {"disk_stats": rpc_json.get("disk_usage_summary")}
    if "project" in rpc_json.get("disk_usage_summary"):
        disk_stats["disk_stats"]["projects"] = (
            [project for project in rpc_json["disk_usage_summary"]["project"]]
            if type(rpc_json["disk_usage_summary"]["project"]) == list
            else [rpc_json["disk_usage_summary"]["project"]]
        )
        del disk_stats["disk_stats"]["project"]
    else:
        disk_stats["disk_stats"]["projects"] = []
    return disk_stats
