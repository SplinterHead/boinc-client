import xmltodict

from boinc_client.clients.rpc_client import RpcClient
from boinc_client.models.public_notice import Notices


def _format_message(message):
    return {
        "project": message["project"],
        "pri": message["pri"],
        "body": message["body"],
        "time": int(message["time"]),
    }


def messages(client: RpcClient, start: int = 0) -> dict:
    """Show messages with sequence numbers beyond the given seqno."""
    rpc_resp = client.make_request(
        f"<get_messages><seqno>{start}</seqno></get_messages>"
    )
    rpc_json = xmltodict.parse(rpc_resp, force_list="msg")
    return {
        "messages": {m["seqno"]: _format_message(m) for m in rpc_json["msgs"]["msg"]}
    }


def message_count(client: RpcClient) -> dict:
    """Show the largest message seqno."""
    rpc_resp = client.make_request("<get_message_count/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return {"message_count": int(rpc_json["seqno"])}


def public_notices(client: RpcClient, start: int = 0) -> dict:
    """Returns only non-private notices, doesn't require authentication."""
    rpc_resp = client.make_request(
        f"<get_notices_public><seqno>{start}</seqno></get_notices_public>"
    )
    rpc_json = xmltodict.parse(rpc_resp, force_list="notice")
    return Notices().load(rpc_json)
