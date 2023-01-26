from pyboinc.reports import get_daily_transfers


def test_can_get_daily_transfer_reports(
    mocker,
    mock_rpc_client,
    daily_transfer_report_xml,
    daily_transfer_report_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=daily_transfer_report_xml,
    )
    assert get_daily_transfers(client=mock_rpc_client) == daily_transfer_report_dict


def test_can_get_multi_daily_transfer_reports(
    mocker,
    mock_rpc_client,
    multi_daily_transfer_report_xml,
    multi_daily_transfer_report_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=multi_daily_transfer_report_xml,
    )
    assert (
        get_daily_transfers(client=mock_rpc_client) == multi_daily_transfer_report_dict
    )
