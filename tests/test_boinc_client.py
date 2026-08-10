import pytest

from boinc_client import RpcClient
from boinc_client.boinc_client import Boinc


def test_throws_exception_if_socket_target_doesnt_exist():
    with pytest.raises(ConnectionError):
        RpcClient(hostname="localhost", port=65535)


def test_thrown_exception_output_code_is_translated(mocker):
    mocker.patch("socket.socket.connect_ex", return_value=61)
    with pytest.raises(ConnectionError) as conn_exc:
        RpcClient(hostname="localhost", port=65535)
    assert "Error connecting to socket" in str(conn_exc.value)


def test_can_create_api_with_boinc_client(mock_rpc_client):
    assert Boinc(rpc_client=mock_rpc_client)


@pytest.mark.parametrize(
    "method_name,function_name,kwargs",
    [
        ("get_messages", "messages", {"start": 5}),
        ("get_message_count", "message_count", {}),
        ("get_public_notices", "public_notices", {"start": 10}),
        ("get_all_notices", "get_all_notices", {"start": 2}),
        ("get_all_projects", "all_projects", {}),
        ("get_results", "results", {"active_only": True}),
        ("get_old_results", "old_results", {}),
        ("get_network_stats", "daily_network_transfers", {}),
        ("get_project_stats", "project_stats", {}),
        ("get_client_state", "client_state", {}),
        ("get_project_status", "project_status", {}),
        ("get_cc_status", "cc_status", {}),
        ("get_disk_stats", "disk_stats", {}),
        ("get_file_transfers", "file_transfers", {}),
        ("get_host_info", "host_info", {}),
        ("get_simple_gui_info", "simple_gui_info", {}),
        ("get_screensaver_tasks", "screensaver_tasks", {}),
        ("get_client_version", "client_version", {}),
        ("get_client_update", "client_update", {}),
    ],
)
def test_boinc_delegates_keyword_calls(
    mocker, mock_boinc_client, method_name, function_name, kwargs
):
    expected = {"ok": method_name}
    call = mocker.patch(
        f"boinc_client.boinc_client.{function_name}", return_value=expected
    )

    result = getattr(mock_boinc_client, method_name)(**kwargs)

    assert result == expected
    call.assert_called_once_with(client=mock_boinc_client.rpc_client, **kwargs)


def test_boinc_delegates_attach_project(mocker, mock_boinc_client):
    call = mocker.patch(
        "boinc_client.boinc_client.attach_project", return_value={"ok": True}
    )

    result = mock_boinc_client.attach_project("name", "http://example.org", "key")

    assert result == {"ok": True}
    call.assert_called_once_with(
        mock_boinc_client.rpc_client, "name", "http://example.org", "key"
    )


@pytest.mark.parametrize(
    "method_name,function_name,arg",
    [
        ("update_project", "update_project", "http://example.org"),
        ("detach_project", "detach_project", "http://example.org"),
        ("suspend_project", "suspend_project", "http://example.org"),
        ("resume_project", "resume_project", "http://example.org"),
        ("reset_project", "reset_project", "http://example.org"),
    ],
)
def test_boinc_delegates_project_single_arg_calls(
    mocker, mock_boinc_client, method_name, function_name, arg
):
    call = mocker.patch(
        f"boinc_client.boinc_client.{function_name}", return_value={"ok": method_name}
    )

    result = getattr(mock_boinc_client, method_name)(arg)

    assert result == {"ok": method_name}
    call.assert_called_once_with(mock_boinc_client.rpc_client, arg)


def test_boinc_delegates_poll_attach_project(mocker, mock_boinc_client):
    call = mocker.patch(
        "boinc_client.boinc_client.poll_attach_project", return_value={"ok": True}
    )

    result = mock_boinc_client.poll_attach_project()

    assert result == {"ok": True}
    call.assert_called_once_with(mock_boinc_client.rpc_client)


@pytest.mark.parametrize(
    "method_name,function_name",
    [
        ("get_global_prefs_file", "get_global_prefs_file"),
        ("get_global_prefs_override", "get_global_prefs_override"),
        ("get_global_prefs_working", "get_global_prefs_working"),
        ("read_global_prefs_override", "read_global_prefs_override"),
        ("get_proxy_settings", "get_proxy_settings"),
    ],
)
def test_boinc_delegates_positional_client_only_calls(
    mocker, mock_boinc_client, method_name, function_name
):
    call = mocker.patch(
        f"boinc_client.boinc_client.{function_name}", return_value={"ok": method_name}
    )

    result = getattr(mock_boinc_client, method_name)()

    assert result == {"ok": method_name}
    call.assert_called_once_with(mock_boinc_client.rpc_client)


@pytest.mark.parametrize(
    "method_name,function_name",
    [
        ("project_no_more_work", "project_no_more_work"),
        ("project_allow_more_work", "project_allow_more_work"),
    ],
)
def test_boinc_delegates_project_work_mode_calls(
    mocker, mock_boinc_client, method_name, function_name
):
    call = mocker.patch(
        f"boinc_client.boinc_client.{function_name}", return_value={"ok": method_name}
    )
    url = "http://example.org"

    result = getattr(mock_boinc_client, method_name)(url)

    assert result == {"ok": method_name}
    call.assert_called_once_with(client=mock_boinc_client.rpc_client, project_url=url)


@pytest.mark.parametrize(
    "method_name,function_name",
    [
        ("set_global_prefs_override", "set_global_prefs_override"),
        ("update_global_prefs_override", "update_global_prefs_override"),
    ],
)
def test_boinc_delegates_preference_override_calls(
    mocker, mock_boinc_client, method_name, function_name
):
    override = {"max_ncpus_pct": 10}
    call = mocker.patch(
        f"boinc_client.boinc_client.{function_name}", return_value={"ok": method_name}
    )

    result = getattr(mock_boinc_client, method_name)(override)

    assert result == {"ok": method_name}
    call.assert_called_once_with(mock_boinc_client.rpc_client, override)


@pytest.mark.parametrize(
    "method_name,function_name,run_mode,duration",
    [
        ("set_cpu_run_mode", "set_cpu_run_mode", "always", 60),
        ("set_gpu_run_mode", "set_gpu_run_mode", "auto", 0),
        ("set_network_mode", "set_network_mode", "never", 30),
    ],
)
def test_boinc_delegates_run_mode_calls(
    mocker, mock_boinc_client, method_name, function_name, run_mode, duration
):
    call = mocker.patch(
        f"boinc_client.boinc_client.{function_name}", return_value={"ok": method_name}
    )

    result = getattr(mock_boinc_client, method_name)(run_mode, duration)

    assert result == {"ok": method_name}
    call.assert_called_once_with(mock_boinc_client.rpc_client, run_mode, duration)
