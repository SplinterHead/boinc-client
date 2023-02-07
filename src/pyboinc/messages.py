import xmltodict

from pyboinc.clients.rpc_client import RpcClient
from pyboinc.models.message_count import MessageCount


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


def _postprocessor(_, key, value):
    if key == "msg":
        return key, {value["seqno"]: value}
    return key, value


def messages(client: RpcClient, start: int = 0) -> dict:
    """Show messages with sequence numbers beyond the given seqno."""
    rpc_resp = client.make_request(
        f"<get_messages><seqno>{start}</seqno></get_messages>"
    )
    rpc_json = xmltodict.parse(rpc_resp, force_list="msg", postprocessor=_postprocessor)
    print(rpc_json)
    thing = {"new_messages": {i: m for (i, m) in rpc_json["msgs"]["msg"]}}
    print(thing)
    return thing


def message_count(client: RpcClient) -> dict:
    """Show the largest message seqno."""
    rpc_resp = client.make_request("<get_message_count/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return MessageCount.parse_obj(rpc_json).dict()


def public_notices(client: RpcClient, start: int = 0) -> dict:
    """Show the largest message seqno."""
    rpc_resp = client.make_request(
        f"<get_notices_public><seqno>{start}</seqno></get_notices_public>"
    )
    rpc_json = xmltodict.parse(rpc_resp, force_list="notice")
    return {
        "notices": {
            n["seqno"]: _format_notice(n) for n in rpc_json["notices"]["notice"]
        }
    }
