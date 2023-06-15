import pytest

from boinc_client.clients.rpc_client import RpcClient


@pytest.fixture
def nonce():
    return "1198959933.057125"


@pytest.fixture
def password_hash():
    return "a1fd70e55f14bf399fbf244cb4bb32b8"


def test_can_create_rpc_client_with_default_values(mocker):
    mocker.patch("socket.socket.connect")
    client = RpcClient(hostname="localhost")
    assert client.hostname == "localhost"
    assert client.port == 31416


def test_can_create_rpc_client_with_custom_port(mocker):
    mocker.patch("socket.socket.connect")
    client = RpcClient(hostname="localhost", port=12345)
    assert client.port == 12345


def test_can_create_rpc_client_with_custom_timeout(mocker):
    mocker.patch("socket.socket.connect")
    client = RpcClient(hostname="localhost", timeout=30)
    assert client.timeout == 30


def test_can_create_rpc_client_with_password(mocker):
    mocker.patch("socket.socket.connect")
    client = RpcClient(hostname="localhost", password="password")
    assert client.password == "password"


def test_client_can_create_socket_connection(mocker):
    m = mocker.patch("socket.socket.connect")
    _ = RpcClient(hostname="localhost")
    m.assert_called_once_with(("localhost", 31416))


def test_client_start_authentication_when_password_passed(mocker, nonce):
    def mock_call(self, req_string: str):
        return f"<boinc_gui_rpc_reply>\n<nonce>{nonce}</nonce>\n</boinc_gui_rpc_reply>"

    mocker.patch("socket.socket.connect")
    mocker.patch("boinc_client.clients.rpc_client.RpcClient._call", mock_call)
    client = RpcClient(hostname="localhost", password="password")
    assert client.get_nonce() == nonce


def test_client_passes_password_to_target(mocker, nonce, password_hash):
    expected_req_str = f"<auth2>\n<nonce_hash>{password_hash}</nonce_hash>\n</auth2>"

    mocker.patch("socket.socket.connect")
    m_call = mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient._call",
        return_value="<boinc_gui_rpc_reply>\n<authorized/>\n</boinc_gui_rpc_reply>",
    )

    client = RpcClient(hostname="localhost", password="password")
    client.send_password(nonce)
    m_call.assert_called_once_with(req_string=expected_req_str)


def test_client_authentication_completes_auth_flow(mocker, nonce):
    mocker.patch("socket.socket.connect")
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.get_nonce", return_value=nonce
    )
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.send_password",
        return_value="authorized",
    )
    client = RpcClient(hostname="localhost", password="password")
    assert client.authenticate()


def test_client_authentication_raises_error_on_auth_failure(mocker, nonce):
    mocker.patch("socket.socket.connect")
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.get_nonce", return_value=nonce
    )
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient.send_password",
        return_value="unauthorized",
    )
    client = RpcClient(hostname="localhost", password="wrong_password")
    assert not client.authenticate()


def test_client_can_make_custom_calls(mocker):
    mocker.patch("socket.socket.connect")
    m_call = mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient._call", return_value="123"
    )

    client = RpcClient(hostname="localhost")
    client.make_request("<mock_call/>")

    m_call.assert_called_once_with(req_string="<mock_call/>")


def test_client_removes_default_wrapper_tag(mocker):
    mocker.patch("socket.socket.connect")
    mocker.patch(
        "boinc_client.clients.rpc_client.RpcClient._call",
        return_value="<boinc_gui_rpc_reply>\n<request/>\n</boinc_gui_rpc_reply>",
    )

    client = RpcClient(hostname="localhost")
    resp = client.make_request("<mock_call/>")

    assert "boinc_gui_rpc_request" not in resp
