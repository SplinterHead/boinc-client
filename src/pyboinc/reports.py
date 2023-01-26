import datetime as dt

import xmltodict

from pyboinc.clients.rpc_client import RpcClient


def _epoch_to_date(epoch_days: str):
    epoch = dt.date(1970, 1, 1)
    delta = dt.timedelta(days=int(epoch_days))
    return epoch + delta


def get_daily_network_transfers(client: RpcClient):
    """Show network traffic history of the BOINC client. Read from daily_xfer_history.xml."""
    rpc_resp = client.make_request("<get_daily_xfer_history/>")
    rpc_json = xmltodict.parse(rpc_resp)
    daily_xfer = {"daily_transfers": {}}
    if type(rpc_json["daily_xfers"]["dx"]) is list:
        for day in rpc_json["daily_xfers"]["dx"]:
            day_key = _epoch_to_date(day["when"]).strftime("%Y-%m-%d")
            daily_xfer["daily_transfers"][day_key] = {
                "up": float(day["up"]),
                "down": float(day["down"]),
            }
    else:
        day = rpc_json["daily_xfers"]["dx"]
        day_key = _epoch_to_date(day["when"]).strftime("%Y-%m-%d")
        daily_xfer["daily_transfers"][day_key] = {
            "up": float(day["up"]),
            "down": float(day["down"]),
        }
    return daily_xfer
