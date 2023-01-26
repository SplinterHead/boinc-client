import xmltodict

from pyboinc.clients.rpc_client import RpcClient


def messages(client: RpcClient) -> dict:
    """Show messages with sequence numbers beyond the given seqno."""
    rpc_resp = client.make_request("<get_messages/>")
    rpc_json = xmltodict.parse(rpc_resp)
    messages = {"messages": {}}
    msg = rpc_json["msgs"]["msg"]
    messages["messages"][msg["seqno"]] = {
        "project": msg["project"],
        "pri": msg["pri"],
        "body": msg["body"],
        "time": int(msg["time"]),
    }
    return messages


def message_count(client: RpcClient) -> int:
    """Show the largest message seqno."""
    rpc_resp = client.make_request("<get_message_count/>")
    rpc_json = xmltodict.parse(rpc_resp)
    return int(rpc_json["seqno"])
