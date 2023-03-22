import xmltodict

from boinc_client.clients.rpc_client import RpcClient
from boinc_client.models.cc_status import CCStatus
from boinc_client.models.client_state import ClientState
from boinc_client.models.disk_stats import DiskUsage
from boinc_client.models.file_transfer import FileTransfers
from boinc_client.models.host_info import HostInfo
from boinc_client.models.project_status import ProjectStatus
from boinc_client.models.screensaver_tasks import ScreensaverTasks
from boinc_client.models.simple_gui_info import SimpleGuiInfo


def client_state(client: RpcClient) -> dict:
    """Get the entire state."""
    rpc_resp = client.make_request("<get_state/>")
    rpc_json = xmltodict.parse(
        rpc_resp,
        force_list=(
            "app",
            "app_version",
            "gui_url",
            "result",
            "workunit",
        ),
    )
    return ClientState().load(rpc_json)


def project_status(client: RpcClient) -> dict:
    """Show status of all attached projects."""
    rpc_resp = client.make_request("<get_project_status/>")
    rpc_json = xmltodict.parse(rpc_resp, force_list=("project", "gui_url"))
    return ProjectStatus().load(rpc_json)


def cc_status(client: RpcClient) -> dict:
    """Show CPU/GPU/network run modes and network connection status."""
    rpc_resp = client.make_request("<get_cc_status/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return CCStatus().load(rpc_json)


def disk_stats(client: RpcClient) -> dict:
    """Show disk usage by project."""
    rpc_resp = client.make_request("<get_disk_usage/>")
    rpc_json = xmltodict.parse(rpc_resp, force_list=("project",))
    return DiskUsage().load(rpc_json)


def file_transfers(client: RpcClient) -> dict:
    """Show all current file transfers."""
    rpc_resp = client.make_request("<get_file_transfers/>")
    rpc_json = xmltodict.parse(rpc_resp, force_list=("file_transfer",))
    return FileTransfers().load(rpc_json)


def host_info(client: RpcClient) -> dict:
    """Get information about host hardware and usage."""
    rpc_resp = client.make_request("<get_host_info/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return HostInfo().load(rpc_json)


def simple_gui_info(client: RpcClient) -> dict:
    """Show status of projects and active tasks."""
    rpc_resp = client.make_request("<get_simple_gui_info/>")
    rpc_json = xmltodict.parse(rpc_resp, force_list=("project", "result", "gui_url"))
    return SimpleGuiInfo().load(rpc_json)


def screensaver_tasks(client: RpcClient) -> dict:
    """Show status of projects and active tasks."""
    rpc_resp = client.make_request("<get_screensaver_tasks/>")
    rpc_json = xmltodict.parse(rpc_resp, force_list=("result",))
    return ScreensaverTasks().load(rpc_json)
