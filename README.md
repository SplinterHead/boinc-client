# pyBoinc

Python library for interacting with a BOINC client via RPC, with consistent response types

## Usage

### Setup

```python
from pyboinc import Boinc
from pyboinc.clients.rpc_client import RpcClient

# Hostname or IP of the running BOINC client
BOINC_HOSTNAME = "192.168.0.2"

# Create an RPC client to connect to the BOINC socket
rpc_client = RpcClient(hostname=BOINC_HOSTNAME)
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

### Get Client Version
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

### Get CC Status

```python
boinc_client.get_cc_status()
```

Response
```json
{
  "cc_status": {
    "network_status": "2",
    "ams_password_error": "0",
    "task_suspend_reason": "0",
    "task_mode": "2",
    "task_mode_perm": "2",
    "task_mode_delay": "0.000000",
    "gpu_suspend_reason": "0",
    "gpu_mode": "2",
    "gpu_mode_perm": "2",
    "gpu_mode_delay": "0.000000",
    "network_suspend_reason": "0",
    "network_mode": "2",
    "network_mode_perm": "2",
    "network_mode_delay": "0.000000",
    "disallow_attach": "0",
    "simple_gui_only": "0",
    "max_event_log_lines": "2000"
  }
}
```

### Get Disk Stats

```python
boinc_client.get_disk_stats()
```

Response
```json
{
  "disk_stats": {
    "projects": [
      {"master_url": "https://projecta.com", "disk_usage": "30"}
    ],
    "d_total": "100",
    "d_free": "20",
    "d_boinc": "50",
    "d_allowed": "75"
  }
}
```

### Get Daily Network Stats

```python
boinc_client.get_network_stats()
```

```json
{
  "daily_transfers": {
    "2023-01-01": {"up": 1000.000, "down": 6000.000},
    "2023-01-02": {"up": 2000.000, "down": 5000.000}
  }
}
```

### Get Message Count

```python
boinc_client.get_message_count()
```

Response

```json
{
  "message_count": 30
}
```

### Get Messages

```python
boinc_client.get_messages()
```

#### Arguments

| Argument | Description                       | Required | Default |
|----------|-----------------------------------|----------|---------|
| `start`  | ID of the first message to return | No       | 0       |

Response

```json
{
    "messages": {
        "1": {
            "project": "Project A",
            "pri": "proja",
            "body": "This is a Message",
            "time": 1672531200
        },
        "2": {
            "project": "Project B",
            "pri": "projb",
            "body": "This is another Message",
            "time": 1672531300
        }
    }
}
```

### Get Public Notices

```python
boinc_client.get_public_notices()
```

#### Arguments

| Argument | Description                      | Required | Default |
|----------|----------------------------------|----------|---------|
| `start`  | ID of the first notice to return | No       | 0       |

Response

```json
{
    "notices": {
        "1": {
            "title": "Notice A",
            "description": "This is a notice",
            "create_time": 123,
            "arrival_time": 124,
            "is_private": false,
            "project_name": "proja",
            "category": "test",
            "link": "https://linky.link"
        }
    }
}
```

### Get Results

```python
boinc_client.get_results()
```

#### Arguments

| Argument      | Description                                         | Required | Default |
|---------------|-----------------------------------------------------|----------|---------|
| `active_only` | Limits the returned results to only the active ones | No       | False   |

Response

```json
{
    "results": [
        {
            "name": "foo",
            "wu_name": "foo",
            "platform": "foo",
            "version_num": "foo",
            "plan_class": "foo",
            "project_url": "foo",
            "final_cpu_time": "foo",
            "final_elapsed_time": "foo",
            "exit_status": "foo",
            "state": "foo",
            "report_deadline": "foo",
            "received_time": "foo",
            "estimated_cpu_time_remaining": "foo",
            "project_suspended_via_gui": "foo",
            "report_immediately": "foo",
            "active_task": {
                "active_task_state": "foo",
                "app_version_num": "foo",
                "slot": "foo",
                "pid": "foo",
                "scheduler_state": "foo",
                "checkpoint_cpu_time": "foo",
                "fraction_done": "foo",
                "current_cpu_time": "foo",
                "elapsed_time": "foo",
                "swap_size": "foo",
                "working_set_size": "foo",
                "working_set_size_smoothed": "foo",
                "page_fault_rate": "foo",
                "bytes_sent": "foo",
                "bytes_received": "foo",
                "progress_rate": "foo"
            },
            "resources": "foo"
        }
    ]
}
```

### Get Old Results

```python
boinc_client.get_old_results()
```

Response

```json
{
    "old_results": [
        {
            "project_url": "foo",
            "result_name": "foo",
            "app_name": "foo",
            "exit_status": "foo",
            "elapsed_time": "foo",
            "cpu_time": "foo",
            "completed_time": "foo",
            "create_time": "foo"
        }
    ]
}
```