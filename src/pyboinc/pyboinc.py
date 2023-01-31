import xmltodict

from pyboinc.clients.rpc_client import RpcClient

from .messages import message_count, messages, public_notices
from .projects import get_all_projects
from .reports import get_daily_network_transfers
from .results import old_results, results
from .stats import project_stats
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

    def get_message_count(self) -> dict:
        return message_count(client=self.rpc_client)

    def get_messages(self, start: int = 0) -> dict:
        return messages(client=self.rpc_client, start=start)

    def get_public_notices(self) -> dict:
        return public_notices(client=self.rpc_client)

    def get_results(self, active_only: bool = False) -> dict:
        return results(client=self.rpc_client, active_only=active_only)

    def get_old_results(self) -> dict:
        return old_results(client=self.rpc_client)

    def get_project_stats(self) -> dict:
        return project_stats(client=self.rpc_client)
