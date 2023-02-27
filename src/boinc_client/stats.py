import xmltodict

from boinc_client.clients.rpc_client import RpcClient
from boinc_client.models.network_transfers import DailyTransfers
from boinc_client.models.projects_stats import ProjectStats


def daily_network_transfers(client: RpcClient) -> dict:
    """Show network traffic history of the BOINC client. Read from daily_xfer_history.xml."""
    rpc_resp = client.make_request("<get_daily_xfer_history/>")
    rpc_json = xmltodict.parse(rpc_resp, force_list="dx")
    return DailyTransfers().load(rpc_json)


def project_stats(client: RpcClient):
    """Get statistics for the projects the client is attached to."""
    rpc_resp = client.make_request("<get_statistics/>")
    rpc_json = xmltodict.parse(
        rpc_resp, force_list=("project_statistics", "daily_statistics")
    )
    return ProjectStats().load(rpc_json)
