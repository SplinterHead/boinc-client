# pyBoinc

Python API for interacting with a BOINC client via RPC

## Usage

### Setup

```python
from pyboinc import Boinc
from pyboinc.clients.rpc_client import RpcClient

# Hostname or IP of the running BOINC client
BOINC_HOSTNAME="192.168.0.2"

# Create an RPC client to connect to the BOINC socket
rpc_client=RpcClient(hostname=BOINC_HOSTNAME)
rpc_client.authenticate()

# Create a BOINC client to interact with the RPC socket
boinc_client = Boinc(rpc_client=rpc_client)
```

### RPC Client options
The following options can be passed when creating an `RpcClient` instance

| Argument   | Description                                                                | Required | Default |
|------------|----------------------------------------------------------------------------|----------|---------|
| `hostname` | Hostname or IP address of the BOINC client                                 | Yes      | None    |
| `port`     | Exposed port of the BOINC client                                           | No       | 31416   |
| `timeout`  | Seconds to wait for a successful connection to the RPC socket              | No       | 30      |
| `password` | Password to authenticate to the BOINC client, required for most operations | No       | None    |

### Boinc options
The following options can be passed when creating a `Boinc` instance

| Argument     | Description                        | Required | Default |
|--------------|------------------------------------|----------|---------|
| `rpc_client` | Instance of a configured RpcClient | Yes      | None    |

## Unauthorised Operations
These operations can be used without supplying a password. They are all read-only for pulling information about a BOINC client

### Get client Version
```python
boinc_client.client_version()
```

Response
```json
{
  "major": "1",
  "minor": "2",
  "release": "0"
}
```

### Get BOINC Projects
```python
boinc_client.get_all_projects()
```

Response
```json
{
  "projects": [
    {
      "name": "SIDock@home",
      "id": "51",
      "url": "https://www.sidock.si/sidock/",
      "web_url": "https://www.sidock.si/sidock/",
      "general_area": "Biology and Medicine",
      "specific_area": "Biomedicine",
      "description": "Study drugs to fight SARS-CoV-2",
      "home": "The COVID.SI project and the Karelian Research Center of the Russian Academy of Sciences",
      "platforms": [
        {"name": "x86_64-pc-linux-gnu"},
        {"name": "x86_64-apple-darwin"},
        {"name": "windows_x86_64"},
        {"name": "arm-unknown-linux-gnueabihf"},
        {"name": "x86_64-openwrt-linux-musl"}
      ],
      "image": "https://boinc.berkeley.edu/images/sidock.png",
      "summary": "Study drugs to fight SARS-CoV-2",
      "keywords": "9 13 64 20 44"
    }
  ]
}
```
