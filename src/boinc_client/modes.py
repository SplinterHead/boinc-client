import xmltodict

from boinc_client.clients.rpc_client import RpcClient
from boinc_client.models.generic_response import GenericResponse


def set_cpu_run_mode(client: RpcClient, run_mode: str, duration: int = 0):
    if run_mode in ["always", "never", "auto", "restore"]:
        req_string = f"<set_run_mode><{run_mode}/>"
        if duration > 0:
            req_string += f"<duration>{duration}</duration>"
        req_string += "</set_run_mode>"
        rpc_resp = client.make_request(req_string)
        rpc_json = xmltodict.parse(rpc_resp)
        return GenericResponse().load(rpc_json)
    return {
        "error": "Invalid CPU mode given. Select from: always, never, auto or restore"
    }
