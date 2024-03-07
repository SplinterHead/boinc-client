import xmltodict
from marshmallow import ValidationError

from boinc_client.clients.rpc_client import RpcClient
from boinc_client.models.generic_response import GenericResponse
from boinc_client.models.global_preference_override import GlobalPreferenceOverrides
from boinc_client.models.global_preferences import GlobalPreferences


def get_global_prefs_file(client: RpcClient) -> dict:
    """Get the contents of the global_prefs.xml file if present."""
    rpc_resp = client.make_request("<get_global_prefs_file/>")
    rpc_json = xmltodict.parse(rpc_resp)
    try:
        return GlobalPreferences().load(rpc_json)
    except ValidationError:
        return GenericResponse().load(rpc_json)


def get_global_prefs_override(client: RpcClient):
    """Get the contents of the global_prefs_override.xml file if present."""
    rpc_resp = client.make_request("<get_global_prefs_override/>")
    rpc_json = xmltodict.parse(rpc_resp)
    try:
        return GlobalPreferenceOverrides().load(rpc_json)
    except ValidationError:
        return GenericResponse().load(rpc_json)


def get_global_prefs_working(client: RpcClient):
    """Get the currently used global_prefs."""
    rpc_resp = client.make_request("<get_global_prefs_working/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return GlobalPreferences().load(rpc_json)


def set_global_prefs_override(client: RpcClient, override: dict):
    """Write the global_prefs_override.xml file."""
    override_xml = "".join([f"<{k}>{v}</{k}>" for k, v in override.items()])
    rpc_resp = client.make_request(
        f"""<set_global_prefs_override>
        <global_preferences>
        {override_xml}
        </global_preferences>
        </set_global_prefs_override>"""
    )
    rpc_json = xmltodict.parse(rpc_resp)
    return GenericResponse().load(rpc_json)


def read_global_prefs_override(client: RpcClient):
    """Read the global_prefs_override.xml file and set the preferences accordingly."""
    rpc_resp = client.make_request("<read_global_prefs_override/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return GenericResponse().load(rpc_json)


############
# Helpers
############
def update_global_prefs_override(client: RpcClient, override: dict):
    """Helper for updating global prefs without resetting others."""
    current_overrides = get_global_prefs_override(client)
    if "error" in current_overrides:
        merged_overrides = override
    else:
        merged_overrides = {**current_overrides["global_preferences"], **override}
    set_global_prefs_override(client, merged_overrides)
