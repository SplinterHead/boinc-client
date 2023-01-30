import xmltodict

from pyboinc.clients.rpc_client import RpcClient


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
    rpc_json = xmltodict.parse(rpc_resp)
    msg = rpc_json["msgs"]["msg"]
    if type(msg) is dict:
        msg = [msg]
    messages = {"messages": {}}
    for m in msg:
        messages["messages"][m["seqno"]] = _format_message(m)
    return messages


def message_count(client: RpcClient) -> int:
    """Show the largest message seqno."""
    rpc_resp = client.make_request("<get_message_count/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return int(rpc_json["seqno"])
