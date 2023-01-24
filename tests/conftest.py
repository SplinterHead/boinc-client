from pytest import fixture

from pyboinc.clients.rpc_client import RpcClient
from pyboinc.pyboinc import Boinc


@fixture
def mock_rpc_client(mocker) -> RpcClient:
    mocker.patch("socket.create_connection")
    return RpcClient(hostname="localhost", port=12345)


@fixture
def mock_boinc_client(mock_rpc_client) -> Boinc:
    return Boinc(rpc_client=mock_rpc_client)


@fixture
def server_version() -> str:
    return "<server_version>\n<major>1</major>\n<minor>2</minor>\n<release>0</release>\n</server_version>"


@fixture
def server_version_dict() -> dict:
    return {"major": "1", "minor": "2", "release": "0"}
