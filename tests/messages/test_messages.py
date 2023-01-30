from pyboinc.messages import message_count, messages


def test_can_get_message_count(mocker, mock_rpc_client):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value="<seqno>1</seqno>",
    )
    assert message_count(client=mock_rpc_client) == 1


def test_can_get_single_message(
    mocker, mock_rpc_client, single_messages_list, single_messages_dict
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=single_messages_list,
    )
    assert messages(client=mock_rpc_client) == single_messages_dict


def test_can_get_multiple_message(
    mocker, mock_rpc_client, multi_messages_list, multi_messages_dict
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=multi_messages_list,
    )
    assert messages(client=mock_rpc_client) == multi_messages_dict
