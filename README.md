# BOINC Client

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

## Contributing

This project uses [Poetry](https://python-poetry.org/) to manage dependencies, environments and execution.
It also uses [Docker](https://www.docker.com/) for running integration tests

Install all dependencies:
```bash
poetry install
```
Everything should be covered by tests, this project has been put together following TDD using `pytest`

Check all the tests are executing properly:
```bash
# Run only the Unit tests
poetry run pytest -m "not integration"

# Run only the Integration tests
poetry run pytest -m integration

# Run all tests (recommended)
poetry run pytest
```

Once changes have been made, use `black` and `isort` to format all the files:
```bash
# Format with black
poetry run black src/ tests/

# Format with isort
poetry run isort --profile=black src/ tests/
```