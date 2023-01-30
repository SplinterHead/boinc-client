from pyboinc.results import results


def test_can_get_single_result(
    mocker,
    mock_rpc_client,
    single_result_xml,
    single_result_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=single_result_xml,
    )
    assert results(client=mock_rpc_client) == single_result_dict


def test_can_get_multiple_result(
    mocker,
    mock_rpc_client,
    multi_result_xml,
    multi_result_dict,
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=multi_result_xml,
    )
    assert results(client=mock_rpc_client) == multi_result_dict
