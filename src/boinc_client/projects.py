import xmltodict

from boinc_client.clients.rpc_client import RpcClient


def all_projects(client: RpcClient) -> dict:
    """Used to get a list of all the projects as found in the all_projects_list.xml file."""
    rpc_resp = client.make_request("<get_all_projects_list/>")
    if rpc_resp == "":
        projects_list = []
    else:
        rpc_json = xmltodict.parse(rpc_resp, force_list="project")
        projects_list = rpc_json["projects"]["project"]
        for project in projects_list:
            project["platforms"] = (
                [{"name": p} for p in project["platforms"]["name"]]
                if type(project["platforms"]["name"]) == list
                else [project["platforms"]]
            )
    return {"projects": projects_list}
