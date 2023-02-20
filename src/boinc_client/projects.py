import xmltodict

from boinc_client.clients.rpc_client import RpcClient
from boinc_client.models.projects import Projects

EMPTY_PROJECT_LIST = "<projects></projects>"


def all_projects(client: RpcClient) -> dict:
    """Used to get a list of all the projects as found in the all_projects_list.xml file."""
    rpc_resp = client.make_request("<get_all_projects_list/>")
    if rpc_resp == "":
        rpc_resp = EMPTY_PROJECT_LIST
    rpc_json = xmltodict.parse(rpc_resp, force_list="project")
    return Projects().load(rpc_json)
