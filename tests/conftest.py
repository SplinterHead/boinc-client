import pytest

from pyboinc.clients.rpc_client import RpcClient


@pytest.fixture
def mock_rpc_client(mocker):
    mocker.patch("socket.create_connection")
    return RpcClient(hostname="localhost", port=12345)
