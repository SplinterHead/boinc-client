import xmltodict

from pyboinc.clients.rpc_client import RpcClient


def get_all_projects(client: RpcClient):
    """Used to get a list of all the projects as found in the all_projects_list.xml file."""
    rpc_resp = client.make_request("<get_all_projects_list/>")
    rpc_json = xmltodict.parse(rpc_resp)
    projects_list = {
        "projects": (
            rpc_json["projects"]["project"]
            if type(rpc_json["projects"]["project"]) == list
            else [rpc_json["projects"]["project"]]
        )
    }
    for project in projects_list.get("projects"):
        project["platforms"] = (
            [{"name": p} for p in project["platforms"]["name"]]
            if type(project["platforms"]["name"]) == list
            else [project["platforms"]]
        )
    return projects_list
