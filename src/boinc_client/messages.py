import xmltodict

from boinc_client.clients.rpc_client import RpcClient


def _format_message(message):
    return {
        "project": message["project"],
        "pri": message["pri"],
        "body": message["body"],
        "time": int(message["time"]),
    }


def _format_notice(notice):
    return {
        "arrival_time": int(notice["arrival_time"]),
        "category": notice["category"],
        "create_time": int(notice["create_time"]),
        "description": notice["description"],
        "is_private": notice["is_private"] == "true",
        "link": notice["link"],
        "project_name": notice["project_name"],
        "title": notice["title"],
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
    return {
        "notices": {
            n["seqno"]: _format_notice(n) for n in rpc_json["notices"]["notice"]
        }
        if rpc_json["notices"]
        else {}
    }
