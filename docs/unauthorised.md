## Unauthorised Operations
These operations are all read-only for pulling information about a BOINC client

### Get Client Version
```python
boinc_client.get_client_version()
```
Response
```python
{
    "version": {
        "major": 1,
        "minor": 2,
        "release": 0
    }
}
```

### Get Client Update
```python
boinc_client.get_client_update()
```
Response
```python
{
    "update": {
        "newer_version": "1.3.0",
        "download_url": "https://boinc.berkeley.edu/download.php"
    }
}
```

### Get BOINC Projects
```python
boinc_client.get_all_projects()
```
Response
```python
{
    "projects": [
        {
            "id": 51,
            "name": "SIDock@home",
            "url": "https://www.sidock.si/sidock/",
            "web_url": "https://www.sidock.si/sidock/",
            "general_area": "Biology and Medicine",
            "specific_area": "Biomedicine",
            "description": "Study drugs to fight SARS-CoV-2",
            "home": "The COVID.SI project and the Karelian Research Center of the Russian Academy of Sciences",
            "platforms": [
                {"name": "x86_64-pc-linux-gnu"}
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
```python
{
    "client_state": {
        "host_info": {},
        "net_stats": {},
        "time_stats": {},
        "project": {},
        "apps": [],
        "app_versions": [],
        "workunits": [],
        "results": [],
        "platform_name": "x86_64-pc-linux-gnu",
        "core_client_major_version": 7,
        "core_client_minor_version": 16,
        "core_client_release": 17,
        "executing_as_daemon": False,
        "platform": "x86_64-pc-linux-gnu",
        "global_preferences": {}
  }
}
```

### Get Project State
```python
boinc_client.get_project_status()
```
Response
```python
{
    "project_status": [
        {
            "master_url": "http://www.worldcommunitygrid.org/",
            "project_name": "World Community Grid",
            "symstore": None,
            "user_name": "user_name",
            "team_name": None,
            "host_venue": None,
            "email_hash": "35cfa58b4e0b46de6a651ce508082d61",
            "cross_project_id": "037befc40287d29bb9590d8e0edd8198",
            "external_cpid": "192792945b257453b6da6c7cad1c1381",
            "cpid_time": 1665410370.000000,
            "user_total_credit": 341094.533876,
            "user_expavg_credit": 2900.946548,
            "user_create_time": 1665410370.000000,
            "rpc_seqno": 655,
            "userid": 1156486,
            "teamid": 0,
            "hostid": 8667640,
            "host_total_credit": 339691.861332,
            "host_expavg_credit": 2900.715440,
            "host_create_time": 1665650589.000000,
            "nrpc_failures": 0,
            "master_fetch_failures": 0,
            "min_rpc_time": 1677187523.062822,
            "next_rpc_time": 1677446601.862822,
            "rec": 4267.417546,
            "rec_time": 1677189666.165000,
            "resource_share": 100.000000,
            "disk_usage": 1410613248.000000,
            "disk_share": 410497975500.800049,
            "desired_disk_usage": 0.000000,
            "duration_correction_factor": 1.000000,
            "sched_rpc_pending": 0,
            "send_time_stats_log": 0,
            "send_job_log": 0,
            "njobs_success": 3872,
            "njobs_error": 86,
            "elapsed_time": 43580057.333979,
            "last_rpc_time": 1677187401.862822,
            "dont_use_dcf": True,
            "rsc_backoff_time": {"name": "CPU", "value": 0.000000},
            "rsc_backoff_interval": {"name": "CPU", "value": 0.000000},
            "gui_urls": [
                {
                    "name": "Research Overview",
                    "description": "Learn about the projects hosted at World Community Grid",
                    "url": "https://www.worldcommunitygrid.org/research/viewAllProjects.do"
                }
            ],
            "sched_priority": -1.041667,
            "project_files_downloaded_time": 0.000000,
            "project_dir": "/var/lib/boinc/projects/www.worldcommunitygrid.org",
            "suspended_via_gui": False,
        }
    ]
}
```

### Get CC Status
```python
boinc_client.get_cc_status()
```
Response
```python
{
    "cc_status": {
        "network_status": 0,
        "ams_password_error": 0,
        "task_suspend_reason": 0,
        "task_mode": 2,
        "task_mode_perm": 2,
        "task_mode_delay": 0.000000,
        "gpu_suspend_reason": 0,
        "gpu_mode": 2,
        "gpu_mode_perm": 2,
        "gpu_mode_delay": 0.000000,
        "network_suspend_reason": 0,
        "network_mode": 2,
        "network_mode_perm": 2,
        "network_mode_delay": 0.000000,
        "disallow_attach": 0,
        "simple_gui_only": 0,
        "max_event_log_lines": 2000
    }
}
```

### Get Disk Stats
```python
boinc_client.get_disk_stats()
```
Response
```python
{
    "disk_stats": {
        "projects": [
            {
                "master_url": "http://www.worldcommunitygrid.org/",
                "disk_usage": 207761408.000000,
            }
        ],
        "d_total": 982809350144.000000,
        "d_free": 374939525120.000000,
        "d_boinc": 12058624.000000,
        "d_allowed": 374085603328.000000,
    }
}
```

### Get File Transfers
```python
boinc_client.get_file_transfers()
```
Response
```python
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
```python
{
    "host_info": {
        "timezone": 0,
        "domain_name": "boincclient.local",
        "ip_addr": "10.10.10.10",
        "host_cpid": "66ad08359a0d486d9f44edd5ca67422e",
        "p_ncpus": 32,
        "p_vendor": "GenuineIntel",
        "p_model": "Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz [Family 6 Model 45 Stepping 7]",
        "p_features": "fpu vme de pse tsc",
        "p_fpops": 4245100250.752763,
        "p_iops": 96143762530.234589,
        "p_membw": 1000000000.000000,
        "p_calculated": 1676897876.373423,
        "p_vm_extensions_disabled": False,
        "m_nbytes": 42097815552.000000,
        "m_cache": 20971520.000000,
        "m_swap": 1034940416.000000,
        "d_total": 982809350144.000000,
        "d_free": 380486336512.000000,
        "os_name": "Linux Ubuntu",
        "os_version": "Ubuntu 20.04.2 LTS [6.0.0-0.deb11.2-amd64|libc 2.31 (Ubuntu GLIBC 2.31-0ubuntu9.2)]",
        "n_usable_coprocs": 0,
        "coprocs": [],
        "wsl_available": False,
    }
}
```

### Get Simple GUI Info
```python
boinc_client.get_simple_gui_info()
```
Response (abridged)
```python
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
```python
{
    "screensaver_tasks": {
        "suspend_reason": 0,
        "results": [
            {
                "name": "MCM1_0196982_3287_1",
                "wu_name": "MCM1_0196982_3287",
                "platform": "x86_64-pc-linux-gnu",
                "version_num": 761,
                "plan_class": None,
                "project_url": "http://www.worldcommunitygrid.org/",
                "final_cpu_time": 0.000000,
                "final_elapsed_time": 0.000000,
                "exit_status": 0,
                "state": 2,
                "report_deadline": 1677501678.000000,
                "received_time": 1676983278.925136,
                "estimated_cpu_time_remaining": 4153.559242,
                "ready_to_report": True,
                "edf_scheduled": False,
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
```python
{
    "project_stats": [
        {
            "master_url": "http://www.worldcommunitygrid.org/",
            "daily_statistics": {
                "2023-01-22": {
                    "user_total_credit": 252425.687796,
                    "user_expavg_credit": 1433.823904,
                    "host_total_credit": 251023.015252,
                    "host_expavg_credit": 1428.390798,
                }
            },
        }
    ]
}
```

### Get Daily Network Stats
```python
boinc_client.get_network_stats()
```
Response
```python
{
    "network_transfers": {
        "2023-01-01": {"up": 1000.000, "down": 6000.000},
        "2023-01-02": {"up": 2000.000, "down": 5000.000},
    }
}
```

### Get Message Count
```python
boinc_client.get_message_count()
```
Response
```python
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
```python
{
    "messages": {
        109: {
            "project": "World Community Grid",
            "pri": "1",
            "body": "Finished download of MCM1_FILENAME.txt",
            "time": 1676897897,
        },
        110: {
            "project": "World Community Grid",
            "pri": "1",
            "body": "Started download of MCM2_FILENAME.txt",
            "time": 1676897897,
        },
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
```python
{
    "notices": {
        1: {
            "title": "Notice A",
            "description": "This is a notice",
            "create_time": 123,
            "arrival_time": 124,
            "is_private": False,
            "project_name": "proja",
            "category": "test",
            "link": "https://linky.link",
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
```python
{
    "results": [
        {
            "name": "MCM1_0196917_6756_0",
            "wu_name": "MCM1_0196917_6756",
            "platform": "x86_64-pc-linux-gnu",
            "version_num": 761,
            "plan_class": None,
            "project_url": "http://www.worldcommunitygrid.org/",
            "final_cpu_time": 0.000000,
            "final_elapsed_time": 0.000000,
            "exit_status": 0,
            "state": 2,
            "report_deadline": 1677415612.000000,
            "received_time": 1676897213.611195,
            "estimated_cpu_time_remaining": 11407.838430,
            "edf_scheduled": True,
            "active_task": {},
            "ready_to_report": False,
        }
    ]
}
```

### Get Old Results
```python
boinc_client.get_old_results()
```
Response
```python
{
    "old_results": [
        {
            "project_url": "http://www.worldcommunitygrid.org/",
            "result_name": "MCM1_0196482_6934_1",
            "app_name": "mcm1",
            "exit_status": 0,
            "elapsed_time": 18639.571019,
            "cpu_time": 18519.400000,
            "completed_time": 1676907410.367930,
            "create_time": 1676907414.380763,
        }
    ]
}
```