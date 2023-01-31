import xmltodict

from pyboinc.clients.rpc_client import RpcClient


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
