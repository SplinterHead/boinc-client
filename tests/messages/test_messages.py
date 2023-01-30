from pyboinc.messages import message_count, messages, public_notices


def test_can_get_message_count(mocker, mock_rpc_client):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value="<seqno>1</seqno>",
    )
    assert message_count(client=mock_rpc_client) == {"message_count": 1}


def test_can_get_single_message(
    mocker, mock_rpc_client, single_messages_xml, single_messages_dict
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=single_messages_xml,
    )
    assert messages(client=mock_rpc_client) == single_messages_dict


def test_can_get_multiple_message(
    mocker, mock_rpc_client, multi_messages_xml, multi_messages_dict
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=multi_messages_xml,
    )
    assert messages(client=mock_rpc_client) == multi_messages_dict


def test_can_get_messages_since_id(
    mocker, mock_rpc_client, multi_messages_xml, multi_messages_dict
):
    m_call = mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=multi_messages_xml,
    )
    _ = messages(client=mock_rpc_client, start=5) == multi_messages_dict
    m_call.assert_called_once_with("<get_messages><seqno>5</seqno></get_messages>")


def test_can_get_single_public_notice(
    mocker, mock_rpc_client, single_notice_xml, single_notice_dict
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=single_notice_xml,
    )
    assert public_notices(client=mock_rpc_client) == single_notice_dict


def test_can_get_multi_public_notice(
    mocker, mock_rpc_client, multi_notice_xml, multi_notice_dict
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=multi_notice_xml,
    )
    assert public_notices(client=mock_rpc_client) == multi_notice_dict


def test_can_get_notices_since_id(
    mocker, mock_rpc_client, multi_notice_xml, multi_notice_dict
):
    m_call = mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=multi_notice_xml,
    )
    _ = public_notices(client=mock_rpc_client, start=5) == multi_notice_dict
    m_call.assert_called_once_with(
        "<get_notices_public><seqno>5</seqno></get_notices_public>"
    )
