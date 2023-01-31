import datetime as dt

import xmltodict

from pyboinc.clients.rpc_client import RpcClient


def _epoch_to_date(epoch_days: str) -> dt.date:
    epoch = dt.date(1970, 1, 1)
    delta = dt.timedelta(days=int(epoch_days))
    return epoch + delta


def daily_network_transfers(client: RpcClient) -> dict:
    """Show network traffic history of the BOINC client. Read from daily_xfer_history.xml."""
    rpc_resp = client.make_request("<get_daily_xfer_history/>")
    rpc_json = xmltodict.parse(rpc_resp)
    daily_xfer = {"network_stats": {}}
    if type(rpc_json["daily_xfers"]["dx"]) is list:
        for day in rpc_json["daily_xfers"]["dx"]:
            day_key = _epoch_to_date(day["when"]).strftime("%Y-%m-%d")
            daily_xfer["network_stats"][day_key] = {
                "up": float(day["up"]),
                "down": float(day["down"]),
            }
    else:
        day = rpc_json["daily_xfers"]["dx"]
        day_key = _epoch_to_date(day["when"]).strftime("%Y-%m-%d")
        daily_xfer["network_stats"][day_key] = {
            "up": float(day["up"]),
            "down": float(day["down"]),
        }
    return daily_xfer


def project_stats(client: RpcClient):
    rpc_resp = client.make_request("<get_statistics/>")
    rpc_json = xmltodict.parse(rpc_resp)
    project_stats = {"project_stats": []}
    proj = rpc_json["statistics"]["project_statistics"]
    if type(proj) is dict:
        proj = [proj]
    for p in proj:
        day = p["daily_statistics"]
        if type(day) is dict:
            day = [day]
        daily_stats = {}
        for d in day:
            daily_stats.update(
                {
                    d["day"]: {
                        "host_expavg_credit": d["host_expavg_credit"],
                        "host_total_credit": d["host_total_credit"],
                        "user_expavg_credit": d["user_expavg_credit"],
                        "user_total_credit": d["user_total_credit"],
                    }
                }
            )
        project_stats["project_stats"].append(
            {
                "daily_statistics": daily_stats,
                "master_url": p["master_url"],
            }
        )
    return project_stats
