from pyboinc.clients.rpc_client import RpcClient

from .messages import message_count, messages, public_notices
from .projects import all_projects
from .results import old_results, results
from .stats import daily_network_transfers, project_stats
from .status import cc_status, disk_stats
from .versions import client_update, client_version


class Boinc:
    rpc_client: RpcClient

    def __init__(self, rpc_client: RpcClient):
        self.rpc_client = rpc_client

    def get_client_version(self) -> dict:
        return client_version(client=self.rpc_client)

    def get_client_update(self) -> dict:
        return client_update(client=self.rpc_client)

    def get_all_projects(self) -> dict:
        return all_projects(client=self.rpc_client)

    def get_cc_status(self) -> dict:
        return cc_status(client=self.rpc_client)

    def get_disk_stats(self) -> dict:
        return disk_stats(client=self.rpc_client)

    def get_network_stats(self) -> dict:
        return daily_network_transfers(client=self.rpc_client)

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
