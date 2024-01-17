# BOINC Client

![Test and Release](https://github.com/SplinterHead/boinc-client/actions/workflows/test-and-release.yml/badge.svg)
[![boinc-client](https://snyk.io/advisor/python/boinc-client/badge.svg)](https://snyk.io/advisor/python/boinc-client)
![PyPI - Downloads](https://img.shields.io/pypi/dm/boinc-client)


Python native library for interacting with a BOINC client via RPC. This library has been designed to have consistent response types.

## Usage

### Setup

```python
from boinc_client import Boinc
from boinc_client.clients.rpc_client import RpcClient

# Hostname or IP of the running BOINC client
BOINC_HOSTNAME = "192.168.0.2"

# Create an RPC client to connect to the BOINC socket
rpc_client = RpcClient(hostname=BOINC_HOSTNAME)
rpc_client.authenticate()

# Create a BOINC client to interact with the RPC socket
boinc_client = Boinc(rpc_client=rpc_client)
```

#### RPC Client options
The following options can be passed when creating an `RpcClient` instance

| Argument   | Description                                                                | Required | Default |
|------------|----------------------------------------------------------------------------|----------|---------|
| `hostname` | Hostname or IP address of the BOINC client                                 | Yes      | None    |
| `port`     | Exposed port of the BOINC client                                           | No       | 31416   |
| `timeout`  | Seconds to wait for a successful connection to the RPC socket              | No       | 30      |
| `password` | Password to authenticate to the BOINC client, required for most operations | No       | None    |

#### Boinc options
The following options can be passed when creating a `Boinc` instance

| Argument     | Description                        | Required | Default |
|--------------|------------------------------------|----------|---------|
| `rpc_client` | Instance of a configured RpcClient | Yes      | None    |

### Interacting with Boinc

* [Unauthorised Operations](docs/unauthorised.md)
* [Project Operations](docs/project.md)

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->