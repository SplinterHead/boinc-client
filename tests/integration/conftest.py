import os

import pytest
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs

from boinc_client.boinc_client import Boinc
from boinc_client.clients.rpc_client import RpcClient

BOINC_PORT = 31416
HOST_PORT = 31416
BOINC_PASSWORD = "password"


@pytest.mark.integration
@pytest.fixture(scope="session")
def boinc_test_container() -> DockerContainer:
    boinc_container = DockerContainer("boinc/client")
    boinc_container.with_name("integration-boinc")
    boinc_container.with_bind_ports(BOINC_PORT, HOST_PORT)
    boinc_container.with_env("BOINC_CMD_LINE_OPTIONS", "--allow_remote_gui_rpc")
    boinc_container.with_env("BOINC_GUI_RPC_PASSWORD", BOINC_PASSWORD)

    container = boinc_container.start()
    wait_for_logs(container, "Initialization completed")
    yield container
    container.stop()


@pytest.mark.integration
@pytest.fixture(scope="session")
def rpc_client(boinc_test_container) -> RpcClient:
    client = RpcClient(hostname="localhost", port=BOINC_PORT, password=BOINC_PASSWORD)
    client.authenticate()
    return client


@pytest.mark.integration
@pytest.fixture(scope="session")
def boinc_client(rpc_client) -> Boinc:
    return Boinc(rpc_client=rpc_client)


@pytest.fixture
def project_weak_key() -> str:
    return os.getenv("BOINC_PROJECT_KEY", "mockkey_123456789")
