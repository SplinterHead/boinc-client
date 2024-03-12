import errno
import re
import socket
import threading
from hashlib import md5

from lxml import etree

xml_parser = etree.XMLParser(resolve_entities=False)


class RpcClient:
    hostname: str
    port: int
    timeout: int
    password: str
    socket: socket.socket
    _call_lock: threading.Lock

    def __init__(
        self, hostname: str, port: int = 31416, timeout: int = 30, password: str = None
    ):
        self.hostname = hostname
        self.port = port
        self.timeout = timeout
        self.password = password
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(self.timeout)
        self.create_connection()
        self._call_lock = threading.Lock()

    def create_connection(self) -> socket:
        socket_result = self.socket.connect_ex((self.hostname, self.port))
        if socket_result > 0:
            self.socket.close()
            raise ConnectionError(
                f"Error connecting to socket, {errno.errorcode[socket_result]}"
            )

    def authenticate(self) -> bool:
        if self.password:
            if self.send_password(nonce=self.get_nonce()) == "authorized":
                return True
        return False

    def get_nonce(self) -> str:
        # Docs: https://boinc.berkeley.edu/trac/wiki/GuiRpcProtocol#Authentication
        # Send the auth1 request and return the nonce
        auth1_resp = self._call(req_string="<auth1/>")
        nonce_resp = etree.fromstring(auth1_resp, parser=xml_parser)
        return nonce_resp[0].text

    def send_password(self, nonce: str) -> str:
        # Combine nonce with password and hash
        auth2_cred = md5(f"{nonce}{self.password}".encode()).hexdigest()
        auth2_req = f"<auth2>\n<nonce_hash>{auth2_cred}</nonce_hash>\n</auth2>"
        auth2_resp = etree.fromstring(
            self._call(req_string=auth2_req), parser=xml_parser
        )
        return auth2_resp[0].tag

    def make_request(self, req_str: str) -> str:
        self._call_lock.acquire()
        response = self._call(req_string=req_str)
        self._call_lock.release()
        return re.sub("<(/)?boinc_gui_rpc_reply>(\\n)?", "", response)

    def _call(self, req_string: str) -> str:
        # Send the request
        buf = f"<boinc_gui_rpc_request>\n{req_string}\n</boinc_gui_rpc_request>\003"
        try:
            self.socket.sendall(str.encode(buf))
        except (socket.error, socket.herror, socket.gaierror, socket.timeout):
            raise

        # Receive the response
        response = ""
        while True:
            try:
                resp = self.socket.recv(8192)
                if not resp:
                    raise socket.error("No data from socket")
                n = resp.find(b"\003")
                if not n == -1:
                    response += resp[:n].decode()
                    break
                else:
                    response += resp.decode()
            except socket.error:
                self.socket.close()
                raise
        return response
