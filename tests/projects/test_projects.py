from pyboinc.projects import get_all_projects


def test_can_get_single_project_with_single_platform(
    mocker,
    mock_rpc_client,
    single_project_single_platform_xml,
    single_project_single_platform_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=single_project_single_platform_xml,
    )
    assert (
        get_all_projects(client=mock_rpc_client) == single_project_single_platform_dict
    )


def test_can_get_single_project_with_multiple_platforms(
    mocker,
    mock_rpc_client,
    single_project_multi_platform_xml,
    single_project_multi_platform_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=single_project_multi_platform_xml,
    )
    assert (
        get_all_projects(client=mock_rpc_client) == single_project_multi_platform_dict
    )


def test_can_get_multiple_projects_with_single_platform(
    mocker,
    mock_rpc_client,
    multi_project_single_platform_xml,
    multi_project_single_platform_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=multi_project_single_platform_xml,
    )
    assert (
        get_all_projects(client=mock_rpc_client) == multi_project_single_platform_dict
    )
