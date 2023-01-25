from pyboinc.status import cc_status


def test_get_cc_status(
    mocker, mock_rpc_client, basic_cc_status_xml, basic_cc_status_dict
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=basic_cc_status_xml,
    )
    assert cc_status(client=mock_rpc_client) == basic_cc_status_dict
