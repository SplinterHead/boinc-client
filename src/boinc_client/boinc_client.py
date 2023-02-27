from boinc_client.clients.rpc_client import RpcClient

from .messages import message_count, messages, public_notices
from .projects import all_projects
from .results import old_results, results
from .stats import daily_network_transfers, project_stats
from .status import (
    cc_status,
    client_state,
    disk_stats,
    file_transfers,
    host_info,
    project_status,
    screensaver_tasks,
    simple_gui_info,
)
from .versions import client_update, client_version


class Boinc:
    rpc_client: RpcClient

    def __init__(self, rpc_client: RpcClient):
        self.rpc_client = rpc_client

    # Messages
    def get_messages(self, start: int = 0) -> dict:
        return messages(client=self.rpc_client, start=start)

    def get_message_count(self) -> dict:
        return message_count(client=self.rpc_client)

    def get_public_notices(self, start: int = 0) -> dict:
        return public_notices(client=self.rpc_client, start=start)

    # Projects
    def get_all_projects(self) -> dict:
        return all_projects(client=self.rpc_client)

    # Results
    def get_results(self, active_only: bool = False) -> dict:
        return results(client=self.rpc_client, active_only=active_only)

    def get_old_results(self) -> dict:
        return old_results(client=self.rpc_client)

    # Stats
    def get_network_stats(self) -> dict:
        return daily_network_transfers(client=self.rpc_client)

    def get_project_stats(self) -> dict:
        return project_stats(client=self.rpc_client)

    # Status
    def get_client_state(self) -> dict:
        return client_state(client=self.rpc_client)

    def get_project_status(self) -> dict:
        return project_status(client=self.rpc_client)

    def get_cc_status(self) -> dict:
        return cc_status(client=self.rpc_client)

    def get_disk_stats(self) -> dict:
        return disk_stats(client=self.rpc_client)

    def get_file_transfers(self) -> dict:
        return file_transfers(client=self.rpc_client)

    def get_host_info(self) -> dict:
        return host_info(client=self.rpc_client)

    def get_simple_gui_info(self) -> dict:
        return simple_gui_info(client=self.rpc_client)

    def get_screensaver_tasks(self) -> dict:
        return screensaver_tasks(client=self.rpc_client)

    # Versions
    def get_client_version(self) -> dict:
        return client_version(client=self.rpc_client)

    def get_client_update(self) -> dict:
        return client_update(client=self.rpc_client)
