import xmltodict

from boinc_client.clients.rpc_client import RpcClient
from boinc_client.models.network_transfers import DailyTransfers


def daily_network_transfers(client: RpcClient) -> dict:
    """Show network traffic history of the BOINC client. Read from daily_xfer_history.xml."""
    rpc_resp = client.make_request("<get_daily_xfer_history/>")
    rpc_json = xmltodict.parse(rpc_resp, force_list="dx")
    return DailyTransfers().load(rpc_json)


def project_stats(client: RpcClient):
    rpc_resp = client.make_request("<get_statistics/>")
    rpc_json = xmltodict.parse(
        rpc_resp, force_list=("project_statistics", "daily_statistics")
    )
    project_stats = {"project_stats": []}
    if rpc_json["statistics"]:
        for proj_stats in rpc_json["statistics"]["project_statistics"]:
            daily_stats = {}
            for day_stat in proj_stats["daily_statistics"]:
                daily_stats.update(
                    {
                        day_stat["day"]: {
                            "host_expavg_credit": day_stat["host_expavg_credit"],
                            "host_total_credit": day_stat["host_total_credit"],
                            "user_expavg_credit": day_stat["user_expavg_credit"],
                            "user_total_credit": day_stat["user_total_credit"],
                        }
                    }
                )
            project_stats["project_stats"].append(
                {
                    "daily_statistics": daily_stats,
                    "master_url": proj_stats["master_url"],
                }
            )
    return project_stats
