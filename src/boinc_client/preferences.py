import xmltodict
from marshmallow import ValidationError

from boinc_client.clients.rpc_client import RpcClient
from boinc_client.models.generic_response import GenericResponse
from boinc_client.models.global_preferences import GlobalPreferences


def get_global_prefs_file(client: RpcClient) -> dict:
    """Get the contents of the global_prefs.xml file if present."""
    rpc_resp = client.make_request("<get_global_prefs_file/>")
    rpc_json = xmltodict.parse(rpc_resp)
    try:
        return GlobalPreferences().load(rpc_json)
    except ValidationError:
        return GenericResponse().load(rpc_json)
