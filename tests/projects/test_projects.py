from boinc_client.projects import (
    all_projects,
    attach_project,
    detach_project,
    poll_attach_project,
)


def test_can_get_empty_list(
    mocker,
    mock_rpc_client,
    empty_project_list_xml,
    empty_project_list_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=empty_project_list_xml,
    )
    assert all_projects(client=mock_rpc_client) == empty_project_list_dict


def test_can_get_single_project_with_single_platform(
    mocker,
    mock_rpc_client,
    single_project_single_platform_xml,
    single_project_single_platform_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=single_project_single_platform_xml,
    )
    assert all_projects(client=mock_rpc_client) == single_project_single_platform_dict


def test_can_get_single_project_with_multiple_platforms(
    mocker,
    mock_rpc_client,
    single_project_multi_platform_xml,
    single_project_multi_platform_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=single_project_multi_platform_xml,
    )
    assert all_projects(client=mock_rpc_client) == single_project_multi_platform_dict


def test_can_get_multiple_projects_with_single_platform(
    mocker,
    mock_rpc_client,
    multi_project_single_platform_xml,
    multi_project_single_platform_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=multi_project_single_platform_xml,
    )
    assert all_projects(client=mock_rpc_client) == multi_project_single_platform_dict


def test_can_attach_to_project(
    mocker, mock_rpc_client, mock_project_url, mock_project_key
):
    m = mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value="<success/>",
    )
    assert attach_project(
        client=mock_rpc_client,
        project_url=mock_project_url,
        project_name="Mock Project",
        project_key=mock_project_key,
    ) == {"success": True}
    m.assert_called_with(
        f"""<project_attach>
        <project_url>{mock_project_url}</project_url>
        <project_name>Mock Project</project_name>
        <authenticator>{mock_project_key}</authenticator>
    </project_attach>"""
    )


def test_project_attach_returns_error(
    mocker, mock_rpc_client, mock_project_url, mock_project_key
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value="<error>Already attached to project</error>",
    )
    response = attach_project(
        client=mock_rpc_client,
        project_url=mock_project_url,
        project_name="Mock Project",
        project_key=mock_project_key,
    )
    assert not response["success"]
    assert response["error"] == "Already attached to project"


def test_project_attach_poll_returns_success(
    mocker,
    mock_rpc_client,
    project_attach_poll_success_xml,
    project_attach_poll_success_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=project_attach_poll_success_xml,
    )
    assert (
        poll_attach_project(client=mock_rpc_client) == project_attach_poll_success_dict
    )


def test_project_attach_poll_returns_error(
    mocker,
    mock_rpc_client,
    project_attach_poll_failure_xml,
    project_attach_poll_failure_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=project_attach_poll_failure_xml,
    )
    assert (
        poll_attach_project(client=mock_rpc_client) == project_attach_poll_failure_dict
    )


def test_can_detach_from_project(mocker, mock_rpc_client, mock_project_url):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value="<success/>",
    )
    assert detach_project(client=mock_rpc_client, project_url=mock_project_url) == {
        "success": True
    }


def test_can_return_error_when_detaching_project(
    mocker, mock_rpc_client, mock_project_url
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value="<error>No such project</error>",
    )
    assert detach_project(client=mock_rpc_client, project_url=mock_project_url) == {
        "success": False,
        "error": "No such project",
    }
