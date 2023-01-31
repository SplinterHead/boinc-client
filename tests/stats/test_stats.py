from pyboinc.stats import project_stats


def test_can_get_single_project_single_day_stats(
    mocker,
    mock_rpc_client,
    single_project_single_day_stats_xml,
    single_project_single_day_stats_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=single_project_single_day_stats_xml,
    )
    assert project_stats(client=mock_rpc_client) == single_project_single_day_stats_dict


def test_can_get_single_project_multi_day_stats(
    mocker,
    mock_rpc_client,
    single_project_multi_day_stats_xml,
    single_project_multi_day_stats_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=single_project_multi_day_stats_xml,
    )
    assert project_stats(client=mock_rpc_client) == single_project_multi_day_stats_dict


def test_can_get_multi_project_single_day_stats(
    mocker,
    mock_rpc_client,
    multi_project_single_day_stats_xml,
    multi_project_single_day_stats_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=multi_project_single_day_stats_xml,
    )
    assert project_stats(client=mock_rpc_client) == multi_project_single_day_stats_dict
