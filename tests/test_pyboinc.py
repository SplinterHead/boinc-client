from pyboinc.pyboinc import Boinc


def test_can_create_api_with_boinc_client(mock_rpc_client):
    assert Boinc(rpc_client=mock_rpc_client)
