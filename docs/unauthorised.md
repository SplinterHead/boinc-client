## Unauthorised Operations
These operations are all read-only for pulling information about a BOINC client

### Get Client Version
```python
boinc_client.get_client_version()
```
Response
```json
{
  "major": "1",
  "minor": "2",
  "release": "0"
}
```

### Get Client Update
```python
boinc_client.get_client_update()
```
Response
```json
{
    "update": {
        "newer_version": "1.3.0",
        "download_url": "http://boincclientdownload.info/v1_3_0.exe",
    }
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

### Get Client State
```python
boinc_client.get_client_state()
```
Response (abridged)
```json
{
        "client_state": {
            "host_info": {},
            "net_stats": {},
            "time_stats": {},
            "platform_name": "foo",
            "core_client_major_version": "foo",
            "core_client_minor_version": "foo",
            "core_client_release": "foo",
            "executing_as_daemon": "foo",
            "platform": "foo",
            "global_preferences": {},
        }
    }
```

### Get Project State
```python
boinc_client.get_project_state()
```
Response
```json
{
    "projects": [
        {
            "master_url": "foo",
            "project_name": "foo",
            "symstore": "foo",
            "user_name": "foo",
            "team_name": "foo",
            "host_venue": "foo",
            "email_hash": "foo",
            "cross_project_id": "foo",
            "external_cpid": "foo",
            "cpid_time": "foo",
            "user_total_credit": "foo",
            "user_expavg_credit": "foo",
            "user_create_time": "foo",
            "rpc_seqno": "foo",
            "userid": "foo",
            "teamid": "foo",
            "hostid": "foo",
            "host_total_credit": "foo",
            "host_expavg_credit": "foo",
            "host_create_time": "foo",
            "nrpc_failures": "foo",
            "master_fetch_failures": "foo",
            "min_rpc_time": "foo",
            "next_rpc_time": "foo",
            "rec": "foo",
            "rec_time": "foo",
            "resource_share": "foo",
            "disk_usage": "foo",
            "disk_share": "foo",
            "desired_disk_usage": "foo",
            "duration_correction_factor": "foo",
            "sched_rpc_pending": "foo",
            "send_time_stats_log": "foo",
            "send_job_log": "foo",
            "njobs_success": "foo",
            "njobs_error": "foo",
            "elapsed_time": "foo",
            "last_rpc_time": "foo",
            "dont_use_dcf": "foo",
            "rsc_backoff_time": {"name": "CPU", "value": "foo"},
            "rsc_backoff_interval": {"name": "CPU", "value": "foo"},
            "gui_urls": [
                {
                    "name": "Research Overview",
                    "description": "Learn about the projects hosted at Foo Network",
                    "url": "https://www.foo.org/research/viewAllProjects.do",
                },
            ],
            "sched_priority": "foo",
            "project_files_downloaded_time": "foo",
            "project_dir": "foo",
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

### Get File Transfers
```python
boinc_client.get_file_transfers()
```
Response
```json
{
    "file_transfers": [
        {
            "project_url": "foo",
            "project_name": "foo",
            "name": "foo",
            "nbytes": "foo",
            "max_nbytes": "foo",
            "status": "foo",
            "persistent_file_xfer": {
                "num_retries": "foo",
                "first_request_time": "foo",
                "next_request_time": "foo",
                "time_so_far": "foo",
                "last_bytes_xferred": "foo",
                "is_upload": "foo",
            },
            "file_xfer": {
                "bytes_xferred": "foo",
                "file_offset": "foo",
                "xfer_speed": "foo",
                "url": "foo",
            },
        }
    ]
}
```

### Get Host Info
```python
boinc_client.get_host_info()
```
Response (abridged)
```json
{
    "host_info": {
        "timezone": "foo",
        "domain_name": "foo",
        "ip_addr": "foo",
        "host_cpid": "foo",
        "p_ncpus": "foo",
        "p_vendor": "foo",
        "p_model": "foo",
        "p_features": "foo",
        "p_fpops": "foo",
        "p_iops": "foo",
        "p_membw": "foo",
        "p_calculated": "foo",
        "p_vm_extensions_disabled": "foo",
        "m_nbytes": "foo",
        "m_cache": "foo",
        "m_swap": "foo",
        "d_total": "foo",
        "d_free": "foo",
        "os_name": "foo",
        "os_version": "foo",
        "product_name": "foo",
        "virtualbox_version": "foo",
        "coprocs": {
            "coproc_intel_gpu": {}
        },
        "opencl_cpu_prop": {},
    }
}
```

### Get Simple GUI Info
```python
boinc_client.get_simple_gui_info()
```
Response (abridged)
```json
{
  "gui_info": {
    "projects": [], 
    "results": []
  }
}
```

### Get Screensaver Tasks
```python
boinc_client.get_screensaver_tasks()
```
Response (abridged)
```json
{
        "screensaver_tasks": {
            "suspend_reason": "0",
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
                    "active_task": {},
                },
            ],
        },
    }
```

### Get Project Statistics
```python
boinc_client.get_project_stats()
```
Response
```json
{
    "project_stats": [
        {
            "master_url": "foo_url",
            "daily_statistics": {
                "foo_day": {
                    "user_total_credit": "foo",
                    "user_expavg_credit": "foo",
                    "host_total_credit": "foo",
                    "host_expavg_credit": "foo"
                }
            }
        }
    ]
}
```

### Get Daily Network Stats
```python
boinc_client.get_network_stats()
```
Response
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
Response (abridged)
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
            "active_task": { },
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