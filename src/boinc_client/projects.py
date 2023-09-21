import xmltodict

from boinc_client.clients.rpc_client import RpcClient
from boinc_client.models.generic_response import GenericResponse
from boinc_client.models.project_attach import ProjectAttachPoll
from boinc_client.models.projects import Projects

EMPTY_PROJECT_LIST = "<projects></projects>"


def all_projects(client: RpcClient) -> dict:
    """Used to get a list of all the projects as found in the all_projects_list.xml file."""
    rpc_resp = client.make_request("<get_all_projects_list/>")
    if not rpc_resp:
        rpc_resp = EMPTY_PROJECT_LIST
    rpc_json = xmltodict.parse(rpc_resp, force_list="project")
    return Projects().load(rpc_json)


def attach_project(
    client: RpcClient, project_name: str, project_url: str, project_key: str
) -> dict:
    """Attach the client to a project."""
    request_xml = f"""<project_attach>
        <project_url>{project_url}</project_url>
        <project_name>{project_name}</project_name>
        <authenticator>{project_key}</authenticator>
    </project_attach>"""
    rpc_resp = client.make_request(request_xml)
    rpc_json = xmltodict.parse(rpc_resp)
    return GenericResponse().load(rpc_json)


def poll_attach_project(client: RpcClient) -> dict:
    """Poll the state of a project attachment."""
    request_xml = "<project_attach_poll/>"
    rpc_resp = client.make_request(request_xml)
    rpc_json = xmltodict.parse(rpc_resp, force_list=("message",))
    return ProjectAttachPoll().load(rpc_json)


def update_project(client: RpcClient, project_url: str) -> dict:
    """Update the state of a project."""
    request_xml = f"""<project_update>
        <project_url>{project_url}</project_url>
    </project_update>"""
    rpc_resp = client.make_request(request_xml)
    rpc_json = xmltodict.parse(rpc_resp)
    return GenericResponse().load(rpc_json)


def detach_project(client: RpcClient, project_url: str) -> dict:
    """Detach from a project."""
    request_xml = f"""<project_detach>
        <project_url>{project_url}</project_url>
    </project_detach>"""
    rpc_resp = client.make_request(request_xml)
    rpc_json = xmltodict.parse(rpc_resp)
    return GenericResponse().load(rpc_json)


def suspend_project(client: RpcClient, project_url: str) -> dict:
    """Suspend a project."""
    request_xml = f"""<project_suspend>
        <project_url>{project_url}</project_url>
    </project_suspend>"""
    rpc_resp = client.make_request(request_xml)
    rpc_json = xmltodict.parse(rpc_resp)
    return GenericResponse().load(rpc_json)


def resume_project(client: RpcClient, project_url: str) -> dict:
    """Resume a project."""
    request_xml = f"""<project_resume>
        <project_url>{project_url}</project_url>
    </project_resume>"""
    rpc_resp = client.make_request(request_xml)
    rpc_json = xmltodict.parse(rpc_resp)
    return GenericResponse().load(rpc_json)


def reset_project(client: RpcClient, project_url: str) -> dict:
    """Reset a project."""
    request_xml = f"""<project_reset>
        <project_url>{project_url}</project_url>
    </project_reset>"""
    rpc_resp = client.make_request(request_xml)
    rpc_json = xmltodict.parse(rpc_resp)
    return GenericResponse().load(rpc_json)


def project_no_more_work(client: RpcClient, project_url: str) -> dict:
    """Stop getting new tasks for a project."""
    request_xml = f"""<project_nomorework>
        <project_url>{project_url}</project_url>
    </project_nomorework>"""
    rpc_resp = client.make_request(request_xml)
    rpc_json = xmltodict.parse(rpc_resp)
    return GenericResponse().load(rpc_json)


def project_allow_more_work(client: RpcClient, project_url: str) -> dict:
    """Receive new tasks for a project. Reverse project_nomorework."""
    request_xml = f"""<project_allowmorework>
        <project_url>{project_url}</project_url>
    </project_allowmorework>"""
    rpc_resp = client.make_request(request_xml)
    rpc_json = xmltodict.parse(rpc_resp)
    return GenericResponse().load(rpc_json)
