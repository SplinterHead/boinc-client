import xmltodict

from boinc_client.clients.rpc_client import RpcClient


def client_state(client: RpcClient) -> dict:
    """Get the entire state."""
    rpc_resp = client.make_request("<get_state/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return rpc_json


def project_state(client: RpcClient) -> dict:
    """Show status of all attached projects."""
    rpc_resp = client.make_request("<get_project_status/>")
    rpc_json = xmltodict.parse(rpc_resp, force_list=("project", "gui_url"))
    if rpc_json["projects"]:
        projects = rpc_json["projects"]["project"]
        for p in projects:
            p["gui_urls"] = p["gui_urls"]["gui_url"]
    else:
        projects = []
    return {"projects": projects}


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
    if rpc_json["file_transfers"]:
        for transfer in rpc_json["file_transfers"]["file_transfer"]:
            file_transfers["file_transfers"].append(transfer)
    return file_transfers


def host_info(client: RpcClient) -> dict:
    """Get information about host hardware and usage."""
    rpc_resp = client.make_request("<get_host_info/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return rpc_json


def simple_gui_info(client: RpcClient) -> dict:
    """Show status of projects and active tasks."""
    rpc_resp = client.make_request("<get_simple_gui_info/>")
    rpc_json = xmltodict.parse(rpc_resp, force_list=("project", "result"))
    projects = (
        [proj for proj in rpc_json["simple_gui_info"]["project"]]
        if rpc_json["simple_gui_info"]
        else []
    )
    for project in projects:
        gui_urls = project["gui_urls"]["gui_url"]
        project["gui_urls"] = gui_urls
    results = (
        [res for res in rpc_json["simple_gui_info"]["result"]]
        if rpc_json["simple_gui_info"]
        else []
    )
    return {"gui_info": {"projects": projects, "results": results}}


def screensaver_tasks(client: RpcClient) -> dict:
    """Show status of projects and active tasks."""
    rpc_resp = client.make_request("<get_screensaver_tasks/>")
    rpc_json = xmltodict.parse(rpc_resp, force_list=("result",))
    results = {
        "suspend_reason": rpc_json["handle_get_screensaver_tasks"]["suspend_reason"],
        "results": rpc_json["handle_get_screensaver_tasks"]["result"]
        if "result" in rpc_json["handle_get_screensaver_tasks"]
        else [],
    }
    return {"screensaver_tasks": results}
