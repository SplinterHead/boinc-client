import xmltodict

from pyboinc.clients.rpc_client import RpcClient

from .projects import get_all_projects


class Boinc:
    rpc_client: RpcClient

    def __init__(self, rpc_client: RpcClient):
        self.rpc_client = rpc_client

    def client_version(self) -> dict:
        """Used to get the version of the running core client and send the version of the request's source."""
        rpc_resp = self.rpc_client.make_request("<exchange_versions/>")
        rpc_json = xmltodict.parse(rpc_resp)
        return rpc_json["server_version"]

    def get_all_projects(self) -> dict:
        return get_all_projects(client=self.rpc_client)