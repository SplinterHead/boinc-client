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
    assert str(conn_exc.value) == "Error connecting to socket, ECONNREFUSED"


def test_can_create_api_with_boinc_client(mock_rpc_client):
    assert Boinc(rpc_client=mock_rpc_client)
