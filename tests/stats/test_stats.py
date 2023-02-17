from boinc_client.stats import daily_network_transfers, project_stats


def test_can_get_empty_network_transfer_reports(
    mocker,
    mock_rpc_client,
    empty_network_transfer_report_xml,
    empty_network_transfer_report_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=empty_network_transfer_report_xml,
    )
    assert (
        daily_network_transfers(client=mock_rpc_client)
        == empty_network_transfer_report_dict
    )


def test_can_get_daily_network_transfer_reports(
    mocker,
    mock_rpc_client,
    daily_network_transfer_report_xml,
    daily_network_transfer_report_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=daily_network_transfer_report_xml,
    )
    assert (
        daily_network_transfers(client=mock_rpc_client)
        == daily_network_transfer_report_dict
    )


def test_can_get_multi_daily_network_transfer_reports(
    mocker,
    mock_rpc_client,
    multi_daily_network_transfer_report_xml,
    multi_daily_network_transfer_report_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=multi_daily_network_transfer_report_xml,
    )
    assert (
        daily_network_transfers(client=mock_rpc_client)
        == multi_daily_network_transfer_report_dict
    )


def test_can_get_empty_project_stats(
    mocker,
    mock_rpc_client,
    empty_project_stats_xml,
    empty_project_stats_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=empty_project_stats_xml,
    )
    assert project_stats(client=mock_rpc_client) == empty_project_stats_dict


def test_can_get_single_project_single_day_stats(
    mocker,
    mock_rpc_client,
    single_project_single_day_stats_xml,
    single_project_single_day_stats_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
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
        "boinc_client.clients.rpc_client.RpcClient.make_request",
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
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=multi_project_single_day_stats_xml,
    )
    assert project_stats(client=mock_rpc_client) == multi_project_single_day_stats_dict
