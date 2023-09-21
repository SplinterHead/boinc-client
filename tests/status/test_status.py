from boinc_client.status import (
    cc_status,
    client_state,
    disk_stats,
    file_transfers,
    host_info,
    project_status,
    screensaver_tasks,
    simple_gui_info,
)


def test_get_cc_status(
    mocker, mock_rpc_client, basic_cc_status_xml, basic_cc_status_dict
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
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
        "boinc_client.clients.rpc_client.RpcClient.make_request",
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
        "boinc_client.clients.rpc_client.RpcClient.make_request",
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
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=disk_stats_multi_project_xml,
    )
    assert disk_stats(client=mock_rpc_client) == disk_stats_multi_project_dict


def test_get_empty_file_transfer(
    mocker,
    mock_rpc_client,
    file_transfers_empty_transfer_xml,
    file_transfers_empty_transfer_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=file_transfers_empty_transfer_xml,
    )
    assert file_transfers(client=mock_rpc_client) == file_transfers_empty_transfer_dict


def test_get_single_file_transfer(
    mocker,
    mock_rpc_client,
    file_transfers_single_transfer_xml,
    file_transfers_single_transfer_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=file_transfers_single_transfer_xml,
    )
    assert file_transfers(client=mock_rpc_client) == file_transfers_single_transfer_dict


def test_get_multi_file_transfer(
    mocker,
    mock_rpc_client,
    file_transfers_multi_transfer_xml,
    file_transfers_multi_transfer_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=file_transfers_multi_transfer_xml,
    )
    assert file_transfers(client=mock_rpc_client) == file_transfers_multi_transfer_dict


def test_can_parse_host_info_no_coprocs(
    mocker,
    mock_rpc_client,
    host_info_no_coprocs_xml,
    host_info_no_coprocs_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=host_info_no_coprocs_xml,
    )
    assert host_info(client=mock_rpc_client) == host_info_no_coprocs_dict


def test_can_parse_host_info_no_cpu_detail(
    mocker,
    mock_rpc_client,
    host_info_no_cpu_detail_xml,
    host_info_no_cpu_detail_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=host_info_no_cpu_detail_xml,
    )
    assert host_info(client=mock_rpc_client) == host_info_no_cpu_detail_dict


def test_can_get_simple_gui_info_empty_result(
    mocker,
    mock_rpc_client,
    simple_gui_info_empty_xml,
    simple_gui_info_empty_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=simple_gui_info_empty_xml,
    )
    assert simple_gui_info(client=mock_rpc_client) == simple_gui_info_empty_dict


def test_can_get_simple_gui_info_single_project_single_result(
    mocker,
    mock_rpc_client,
    simple_gui_info_singles_xml,
    simple_gui_info_singles_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=simple_gui_info_singles_xml,
    )
    assert simple_gui_info(client=mock_rpc_client) == simple_gui_info_singles_dict


def test_can_get_simple_gui_info_multi_project_multi_result(
    mocker,
    mock_rpc_client,
    simple_gui_info_multi_xml,
    simple_gui_info_multi_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=simple_gui_info_multi_xml,
    )
    assert simple_gui_info(client=mock_rpc_client) == simple_gui_info_multi_dict


def test_can_get_screensaver_tasks_empty_result(
    mocker,
    mock_rpc_client,
    screensaver_tasks_empty_result_xml,
    screensaver_tasks_empty_result_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=screensaver_tasks_empty_result_xml,
    )
    assert (
        screensaver_tasks(client=mock_rpc_client) == screensaver_tasks_empty_result_dict
    )


def test_can_get_screensaver_tasks_single_result(
    mocker,
    mock_rpc_client,
    screensaver_tasks_single_result_xml,
    screensaver_tasks_single_result_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=screensaver_tasks_single_result_xml,
    )
    assert (
        screensaver_tasks(client=mock_rpc_client)
        == screensaver_tasks_single_result_dict
    )


def test_can_get_screensaver_tasks_multi_result(
    mocker,
    mock_rpc_client,
    screensaver_tasks_multi_result_xml,
    screensaver_tasks_multi_result_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=screensaver_tasks_multi_result_xml,
    )
    assert (
        screensaver_tasks(client=mock_rpc_client) == screensaver_tasks_multi_result_dict
    )


def test_can_get_blank_client_state(
    mocker, mock_rpc_client, blank_client_state_xml, blank_client_state_dict
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=blank_client_state_xml,
    )
    assert client_state(client=mock_rpc_client) == blank_client_state_dict


def test_can_get_client_state(
    mocker, mock_rpc_client, client_state_xml, client_state_dict
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=client_state_xml,
    )
    assert client_state(client=mock_rpc_client) == client_state_dict


def test_can_get_client_state_with_multiple_projects(
    mocker, mock_rpc_client, multi_project_no_result_xml, multi_project_no_result_dict
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=multi_project_no_result_xml,
    )
    assert client_state(client=mock_rpc_client) == multi_project_no_result_dict


def test_can_get_new_project_attach_client_state(
    mocker,
    mock_rpc_client,
    new_project_attach_client_state_xml,
    new_project_attach_client_state_dict,
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=new_project_attach_client_state_xml,
    )
    assert client_state(client=mock_rpc_client) == new_project_attach_client_state_dict


def test_can_get_empty_project_status(
    mocker, mock_rpc_client, empty_project_status_xml, empty_project_status_dict
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=empty_project_status_xml,
    )
    assert project_status(client=mock_rpc_client) == empty_project_status_dict


def test_can_get_project_status(
    mocker, mock_rpc_client, project_status_xml, project_status_dict
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=project_status_xml,
    )
    assert project_status(client=mock_rpc_client) == project_status_dict


def test_can_get_no_more_work_project_status(
    mocker, mock_rpc_client, no_more_work_project_xml, no_more_work_project_dict
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=no_more_work_project_xml,
    )
    assert project_status(client=mock_rpc_client) == no_more_work_project_dict


def test_can_get_allow_more_work_project_status(
    mocker, mock_rpc_client, project_status_xml, project_status_dict
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=project_status_xml,
    )
    assert project_status(client=mock_rpc_client) == project_status_dict


def test_can_get_suspended_project_status(
    mocker, mock_rpc_client, suspended_project_status_xml, suspended_project_status_dict
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=suspended_project_status_xml,
    )
    assert project_status(client=mock_rpc_client) == suspended_project_status_dict
