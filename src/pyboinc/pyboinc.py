import xmltodict

from pyboinc.clients.rpc_client import RpcClient

from .messages import message_count, messages
from .projects import get_all_projects
from .reports import get_daily_network_transfers
from .status import cc_status, disk_stats


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

    def get_cc_status(self) -> dict:
        return cc_status(client=self.rpc_client)

    def get_disk_stats(self) -> dict:
        return disk_stats(client=self.rpc_client)

    def get_network_stats(self) -> dict:
        return get_daily_network_transfers(client=self.rpc_client)

    def get_message_count(self) -> int:
        return message_count(client=self.rpc_client)

    def get_messages(self, start: int = 0) -> dict:
        return messages(client=self.rpc_client, start=start)
