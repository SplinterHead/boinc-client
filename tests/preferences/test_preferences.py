from boinc_client.preferences import get_global_prefs_file


def test_can_get_global_prefs_file(
    mocker, mock_rpc_client, global_prefs_xml, global_prefs_dict
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=global_prefs_xml,
    )
    assert get_global_prefs_file(client=mock_rpc_client) == global_prefs_dict
