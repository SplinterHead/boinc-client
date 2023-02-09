import json

import xmltodict

from pyboinc.status import (
    cc_status,
    disk_stats,
    file_transfers,
    host_info,
    simple_gui_info,
)


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


def test_get_single_file_transfer(
    mocker,
    mock_rpc_client,
    file_transfers_single_transfer_xml,
    file_transfers_single_transfer_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
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
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=file_transfers_multi_transfer_xml,
    )
    assert file_transfers(client=mock_rpc_client) == file_transfers_multi_transfer_dict


def test_can_parse_host_info(
    mocker,
    mock_rpc_client,
    host_info_xml,
    host_info_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=host_info_xml,
    )
    assert host_info(client=mock_rpc_client) == host_info_dict


def test_can_get_simple_gui_info_single_project_single_result(
    mocker,
    mock_rpc_client,
    simple_gui_info_singles_xml,
    simple_gui_info_singles_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
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
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=simple_gui_info_multi_xml,
    )
    assert simple_gui_info(client=mock_rpc_client) == simple_gui_info_multi_dict
