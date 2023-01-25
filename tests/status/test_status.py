from pyboinc.status import cc_status, disk_stats


def test_get_cc_status(
    mocker, mock_rpc_client, basic_cc_status_xml, basic_cc_status_dict
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=basic_cc_status_xml,
    )
    assert cc_status(client=mock_rpc_client) == basic_cc_status_dict


def test_get_disk_stats_with_no_project(
    mocker,
    mock_rpc_client,
    disk_stats_no_project_xml,
    disk_stats_no_project_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=disk_stats_no_project_xml,
    )
    assert disk_stats(client=mock_rpc_client) == disk_stats_no_project_dict


def test_get_disk_stats_for_single_project(
    mocker,
    mock_rpc_client,
    disk_stats_single_project_xml,
    disk_stats_single_project_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=disk_stats_single_project_xml,
    )
    assert disk_stats(client=mock_rpc_client) == disk_stats_single_project_dict


def test_get_disk_stats_for_multi_project(
    mocker,
    mock_rpc_client,
    disk_stats_multi_project_xml,
    disk_stats_multi_project_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=disk_stats_multi_project_xml,
    )
    assert disk_stats(client=mock_rpc_client) == disk_stats_multi_project_dict
