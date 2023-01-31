from pyboinc.versions import client_version


def test_can_get_client_version(
    mocker, mock_rpc_client, server_version_xml, server_version_dict
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=server_version_xml,
    )
    assert client_version(client=mock_rpc_client) == server_version_dict
