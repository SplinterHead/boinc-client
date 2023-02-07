import xmltodict

from pyboinc.clients.rpc_client import RpcClient
from pyboinc.models.project_list import ProjectList


def all_projects(client: RpcClient) -> dict:
    """Used to get a list of all the projects as found in the all_projects_list.xml file."""
    rpc_resp = client.make_request("<get_all_projects_list/>")
    rpc_json = xmltodict.parse(rpc_resp, force_list="project")
    return ProjectList.parse_obj(rpc_json["projects"]).dict()
