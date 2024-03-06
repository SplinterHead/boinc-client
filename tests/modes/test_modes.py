from boinc_client import set_cpu_run_mode
from boinc_client.modes import set_gpu_run_mode


def test_can_set_cpu_run_mode(mocker, mock_rpc_client):
    m = mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value="<success/>",
    )
    assert set_cpu_run_mode(client=mock_rpc_client, run_mode="always") == {
        "success": True
    }
    m.assert_called_with("<set_run_mode><always/></set_run_mode>")


def test_can_set_cpu_run_mode_with_duration(mocker, mock_rpc_client):
    m = mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value="<success/>",
    )
    assert set_cpu_run_mode(client=mock_rpc_client, run_mode="always", duration=60) == {
        "success": True
    }
    m.assert_called_with(
        "<set_run_mode><always/><duration>60</duration></set_run_mode>"
    )


def test_cannot_set_invalid_cpu_run_mode(mocker, mock_rpc_client):
    m = mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value="<error/>",
    )
    assert set_cpu_run_mode(client=mock_rpc_client, run_mode="dummy") == {
        "error": "Invalid CPU mode given. Select from: always, never, auto or restore"
    }
    assert not m.called


def test_can_set_gpu_run_mode(mocker, mock_rpc_client):
    m = mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value="<success/>",
    )
    assert set_gpu_run_mode(client=mock_rpc_client, run_mode="always") == {
        "success": True
    }
    m.assert_called_with("<set_gpu_mode><always/></set_gpu_mode>")


def test_can_set_gpu_run_mode_with_duration(mocker, mock_rpc_client):
    m = mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value="<success/>",
    )
    assert set_gpu_run_mode(client=mock_rpc_client, run_mode="always", duration=60) == {
        "success": True
    }
    m.assert_called_with(
        "<set_gpu_mode><always/><duration>60</duration></set_gpu_mode>"
    )


def test_cannot_set_invalid_gpu_run_mode(mocker, mock_rpc_client):
    m = mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.make_request",
        return_value="<error/>",
    )
    assert set_gpu_run_mode(client=mock_rpc_client, run_mode="dummy") == {
        "error": "Invalid GPU mode given. Select from: always, never, auto or restore"
    }
    assert not m.called
