from pyboinc.pyboinc import Boinc


def test_can_create_api_with_boinc_client(mock_rpc_client):
    assert Boinc(rpc_client=mock_rpc_client)


def test_can_get_client_version(
    mocker, mock_boinc_client, server_version, server_version_dict
):
    mocker.patch(
        "pyboinc.clients.rpc_client.RpcClient.make_request",
        return_value=server_version,
    )
    assert mock_boinc_client.client_version() == server_version_dict
