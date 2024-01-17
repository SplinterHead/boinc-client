from boinc_client.preferences import (
    get_global_prefs_file,
    get_global_prefs_override,
    get_global_prefs_working,
    read_global_prefs_override,
    set_global_prefs_override,
)


def test_can_get_global_prefs_file(
    mocker, mock_rpc_client, global_prefs_xml, global_prefs_dict
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=global_prefs_xml,
    )
    assert get_global_prefs_file(client=mock_rpc_client) == global_prefs_dict


def test_can_handle_no_global_prefs_file(mocker, mock_rpc_client):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value="""<error>-108</error>""",
    )
    assert not get_global_prefs_file(client=mock_rpc_client)["success"]


def test_can_get_global_prefs_override(
    mocker, mock_rpc_client, global_prefs_override_xml, global_prefs_override_dict
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=global_prefs_override_xml,
    )
    assert (
        get_global_prefs_override(client=mock_rpc_client) == global_prefs_override_dict
    )


def test_can_handle_no_global_prefs_override(mocker, mock_rpc_client):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value="""<error>no prefs override file</error>""",
    )
    assert not get_global_prefs_override(client=mock_rpc_client)["success"]


def test_can_get_global_prefs_working(
    mocker, mock_rpc_client, global_prefs_xml, global_prefs_dict
):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value=global_prefs_xml,
    )
    assert get_global_prefs_working(client=mock_rpc_client) == global_prefs_dict


def test_can_set_global_prefs_override(mocker, mock_rpc_client):
    m = mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value="<success/>",
    )
    assert set_global_prefs_override(
        client=mock_rpc_client, override={"mock_key": "mock"}
    ) == {"success": True}
    m.assert_called_with(
        f"""<set_global_prefs_override>
        <global_preferences>
        <mock_key>mock</mock_key>
        </global_preferences>
        </set_global_prefs_override>"""
    )


def test_can_read_global_prefs_override(mocker, mock_rpc_client):
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value="<success/>",
    )
    assert read_global_prefs_override(client=mock_rpc_client) == {"success": True}
