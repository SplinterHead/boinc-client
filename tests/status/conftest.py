from pytest import fixture


@fixture
def basic_cc_status_xml(test_files) -> str:
    return open(f"{test_files}/cc_status/basic_cc_status.xml").read()


@fixture
def basic_cc_status_dict() -> dict:
    return {
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
            "max_event_log_lines": 2000,
        }
    }


@fixture
def disk_stats_no_project_xml(test_files) -> str:
    return open(f"{test_files}/disk_stats/no_project_disk_stats.xml").read()


@fixture
def disk_stats_no_project_dict() -> dict:
    return {
        "disk_stats": {
            "projects": [],
            "d_total": 982809350144.000000,
            "d_free": 374939525120.000000,
            "d_boinc": 12058624.000000,
            "d_allowed": 374085603328.000000,
        }
    }


@fixture
def disk_stats_single_project_xml(test_files) -> str:
    return open(f"{test_files}/disk_stats/single_project_disk_stats.xml").read()


@fixture
def disk_stats_single_project_dict() -> dict:
    return {
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


@fixture
def disk_stats_multi_project_xml(test_files) -> str:
    return open(f"{test_files}/disk_stats/multiple_project_disk_stats.xml").read()


@fixture
def disk_stats_multi_project_dict() -> dict:
    return {
        "disk_stats": {
            "projects": [
                {
                    "master_url": "http://www.worldcommunitygrid.org/",
                    "disk_usage": 207761408.000000,
                },
                {
                    "master_url": "http://www.spacecommunitygrid.org/",
                    "disk_usage": 702261408.000000,
                },
            ],
            "d_total": 982809350144.000000,
            "d_free": 374939525120.000000,
            "d_boinc": 12058624.000000,
            "d_allowed": 374085603328.000000,
        }
    }


@fixture
def file_transfers_empty_transfer_xml(test_files) -> str:
    return open(f"{test_files}/file_transfers/no_file_transfers.xml").read()


@fixture
def file_transfers_empty_transfer_dict() -> dict:
    return {"file_transfers": []}


@fixture
def file_transfers_single_transfer_xml(test_files) -> str:
    return open(f"{test_files}/file_transfers/single_file_transfer.xml").read()


@fixture
def file_transfers_single_transfer_dict() -> dict:
    return {
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


@fixture
def file_transfers_multi_transfer_xml(test_files) -> str:
    return open(f"{test_files}/file_transfers/multi_file_transfer.xml").read()


@fixture
def file_transfers_multi_transfer_dict() -> dict:
    return {
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
            },
            {
                "project_url": "bar",
                "project_name": "bar",
                "name": "bar",
                "nbytes": "bar",
                "max_nbytes": "bar",
                "status": "bar",
                "persistent_file_xfer": {
                    "num_retries": "bar",
                    "first_request_time": "bar",
                    "next_request_time": "bar",
                    "time_so_far": "bar",
                    "last_bytes_xferred": "bar",
                    "is_upload": "bar",
                },
                "file_xfer": {
                    "bytes_xferred": "bar",
                    "file_offset": "bar",
                    "xfer_speed": "bar",
                    "url": "bar",
                },
            },
        ]
    }


@fixture
def host_info_no_coprocs_xml(test_files) -> str:
    return open(f"{test_files}/host_info/host_info_no_coprocs.xml").read()


@fixture
def host_info_no_coprocs_dict() -> dict:
    return {
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


@fixture
def host_info_no_cpu_detail_xml(test_files) -> str:
    return open(f"{test_files}/host_info/host_info_no_cpu_detail.xml").read()


@fixture
def host_info_no_cpu_detail_dict() -> dict:
    return {
        "host_info": {
            "timezone": 0,
            "domain_name": "6435fb00540b",
            "ip_addr": "172.17.0.2",
            "host_cpid": "66ad08359a0d486d9f44edd5ca67422e",
            "p_ncpus": 5,
            "p_vendor": "",
            "p_model": "",
            "p_features": "fpu vme de pse tsc",
            "p_fpops": 1000000000.000000,
            "p_iops": 1000000000.000000,
            "p_membw": 1000000000.000000,
            "p_calculated": 1677059678.204386,
            "p_vm_extensions_disabled": False,
            "m_nbytes": 8232894464.000000,
            "m_cache": -1.000000,
            "m_swap": 1073737728.000000,
            "d_total": 62671097856.000000,
            "d_free": 41954885632.000000,
            "os_name": "Linux Ubuntu",
            "os_version": "Ubuntu 20.04.2 LTS [5.15.49-linuxkit|libc 2.31 (Ubuntu GLIBC 2.31-0ubuntu9.2)]",
            "n_usable_coprocs": 0,
            "coprocs": [],
            "wsl_available": False,
        }
    }


@fixture
def simple_gui_info_empty_xml(test_files) -> str:
    return open(f"{test_files}/simple_gui_info/empty_gui_info.xml").read()


@fixture
def simple_gui_info_empty_dict() -> dict:
    return {"gui_info": {"projects": [], "results": []}}


@fixture
def simple_gui_info_singles_xml(test_files) -> str:
    return open(f"{test_files}/simple_gui_info/simple_gui_info.xml").read()


@fixture
def simple_gui_info_singles_dict() -> dict:
    return {
        "gui_info": {
            "projects": [
                {
                    "master_url": "http://www.worldcommunitygrid.org/",
                    "project_name": "World Community Grid",
                    "symstore": "",
                    "user_name": "user_name",
                    "team_name": "",
                    "host_venue": "",
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
                    "dont_request_more_work": False,
                    "master_url_fetch_pending": False,
                    "scheduler_rpc_in_progress": False,
                    "rsc_backoff_time": {"name": "CPU", "value": 0.000000},
                    "rsc_backoff_interval": {"name": "CPU", "value": 0.000000},
                    "gui_urls": [
                        {
                            "name": "Research Overview",
                            "description": "Learn about the projects hosted at World Community Grid",
                            "url": "https://www.worldcommunitygrid.org/research/viewAllProjects.do",
                        }
                    ],
                    "sched_priority": -1.041667,
                    "project_files_downloaded_time": 0.000000,
                    "project_dir": "/var/lib/boinc/projects/www.worldcommunitygrid.org",
                    "suspended_via_gui": False,
                }
            ],
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
                    "active_task": {
                        "active_task_state": 1,
                        "app_version_num": 761,
                        "slot": 2,
                        "pid": 126,
                        "scheduler_state": 2,
                        "checkpoint_cpu_time": 1805.943000,
                        "fraction_done": 0.242016,
                        "current_cpu_time": 1951.827000,
                        "elapsed_time": 1967.428389,
                        "swap_size": 75472896.000000,
                        "working_set_size": 74682368.000000,
                        "working_set_size_smoothed": 74682368.000000,
                        "page_fault_rate": 0.000000,
                        "bytes_sent": 0.000000,
                        "bytes_received": 0.000000,
                        "progress_rate": 0.000121,
                        "graphics_exec_path": "/var/lib/boinc/projects/www.worldcommunitygrid.org/wcgrid_mcm1_gfx_7.61_x86_64-pc-linux-gnu",
                        "slot_path": "/var/lib/boinc/slots/2",
                    },
                    "ready_to_report": False,
                    "project_suspended_via_gui": False,
                }
            ],
        }
    }


@fixture
def simple_gui_info_multi_xml(test_files) -> str:
    return open(f"{test_files}/simple_gui_info/full_gui_info.xml").read()


@fixture
def simple_gui_info_multi_dict() -> dict:
    return {
        "gui_info": {
            "projects": [
                {
                    "master_url": "http://www.worldcommunitygrid.org/",
                    "project_name": "World Community Grid",
                    "symstore": "",
                    "user_name": "user_name",
                    "team_name": "",
                    "host_venue": "",
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
                    "rec": 4259.828397,
                    "rec_time": 1677188660.726735,
                    "resource_share": 100.000000,
                    "disk_usage": 1410613248.000000,
                    "disk_share": 410497975500.800049,
                    "desired_disk_usage": 0.000000,
                    "duration_correction_factor": 1.000000,
                    "sched_rpc_pending": 0,
                    "send_time_stats_log": 0,
                    "send_job_log": 0,
                    "njobs_success": 3869,
                    "njobs_error": 86,
                    "elapsed_time": 43564806.320009,
                    "last_rpc_time": 1677187401.862822,
                    "dont_use_dcf": True,
                    "dont_request_more_work": False,
                    "master_url_fetch_pending": False,
                    "scheduler_rpc_in_progress": False,
                    "rsc_backoff_time": {"name": "CPU", "value": 0.000000},
                    "rsc_backoff_interval": {"name": "CPU", "value": 0.000000},
                    "gui_urls": [
                        {
                            "name": "Research Overview",
                            "description": "Learn about the projects hosted at World Community Grid",
                            "url": "https://www.worldcommunitygrid.org/research/viewAllProjects.do",
                        },
                        {
                            "name": "News and Updates",
                            "description": "The latest information about World Community Grid and its research projects",
                            "url": "https://www.worldcommunitygrid.org/about_us/displayNews.do",
                        },
                        {
                            "name": "My Contribution",
                            "description": "Your statistics and settings",
                            "url": "https://www.worldcommunitygrid.org/ms/viewMyMemberPage.do",
                        },
                    ],
                    "sched_priority": -1.181306,
                    "project_files_downloaded_time": 0.000000,
                    "project_dir": "/var/lib/boinc/projects/www.worldcommunitygrid.org",
                    "suspended_via_gui": False,
                }
            ],
            "results": [
                {
                    "name": "OPN1_0114551_01118_0",
                    "wu_name": "OPN1_0114551_01118",
                    "platform": "x86_64-pc-linux-gnu",
                    "version_num": 721,
                    "plan_class": None,
                    "project_url": "http://www.worldcommunitygrid.org/",
                    "final_cpu_time": 0.000000,
                    "final_elapsed_time": 0.000000,
                    "exit_status": 0,
                    "state": 2,
                    "report_deadline": 1677698401.000000,
                    "received_time": 1677180001.968065,
                    "estimated_cpu_time_remaining": 338.903730,
                    "edf_scheduled": False,
                    "active_task": {
                        "active_task_state": 1,
                        "app_version_num": 721,
                        "slot": 12,
                        "pid": 229,
                        "scheduler_state": 2,
                        "checkpoint_cpu_time": 8051.674000,
                        "fraction_done": 0.960588,
                        "current_cpu_time": 8221.232000,
                        "elapsed_time": 8292.988796,
                        "swap_size": 262135808.000000,
                        "working_set_size": 202612736.000000,
                        "working_set_size_smoothed": 202612694.781110,
                        "page_fault_rate": 0.000000,
                        "bytes_sent": 0.000000,
                        "bytes_received": 0.000000,
                        "progress_rate": 0.000116,
                        "graphics_exec_path": "/var/lib/boinc/projects/www.worldcommunitygrid.org/wcgrid_opn1_gfx_7.21_x86_64-pc-linux-gnu",
                        "slot_path": "/var/lib/boinc/slots/12",
                    },
                    "ready_to_report": False,
                    "project_suspended_via_gui": False,
                },
                {
                    "name": "OPN1_0114551_01137_0",
                    "wu_name": "OPN1_0114551_01137",
                    "platform": "x86_64-pc-linux-gnu",
                    "version_num": 721,
                    "plan_class": None,
                    "project_url": "http://www.worldcommunitygrid.org/",
                    "final_cpu_time": 0.000000,
                    "final_elapsed_time": 0.000000,
                    "exit_status": 0,
                    "state": 2,
                    "report_deadline": 1677698401.000000,
                    "received_time": 1677180001.968065,
                    "estimated_cpu_time_remaining": 793.453418,
                    "edf_scheduled": False,
                    "active_task": {
                        "active_task_state": 1,
                        "app_version_num": 721,
                        "slot": 13,
                        "pid": 231,
                        "scheduler_state": 2,
                        "checkpoint_cpu_time": 7576.723000,
                        "fraction_done": 0.907728,
                        "current_cpu_time": 7783.957000,
                        "elapsed_time": 7801.396273,
                        "swap_size": 263680000.000000,
                        "working_set_size": 203603968.000000,
                        "working_set_size_smoothed": 203603965.423828,
                        "page_fault_rate": 0.000000,
                        "bytes_sent": 0.000000,
                        "bytes_received": 0.000000,
                        "progress_rate": 0.000117,
                        "graphics_exec_path": "/var/lib/boinc/projects/www.worldcommunitygrid.org/wcgrid_opn1_gfx_7.21_x86_64-pc-linux-gnu",
                        "slot_path": "/var/lib/boinc/slots/13",
                    },
                    "ready_to_report": False,
                    "project_suspended_via_gui": False,
                },
            ],
        }
    }


@fixture
def screensaver_tasks_empty_result_xml(test_files) -> str:
    return open(f"{test_files}/screensaver_tasks/no_result.xml").read()


@fixture
def screensaver_tasks_empty_result_dict() -> dict:
    return {"screensaver_tasks": {"suspend_reason": 0, "results": []}}


@fixture
def screensaver_tasks_single_result_xml(test_files) -> str:
    return open(f"{test_files}/screensaver_tasks/single_result.xml").read()


@fixture
def screensaver_tasks_single_result_dict() -> dict:
    return {
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
                    "ready_to_report": False,
                    "edf_scheduled": False,
                    "active_task": {
                        "active_task_state": 1,
                        "app_version_num": 761,
                        "slot": 14,
                        "pid": 88,
                        "scheduler_state": 2,
                        "checkpoint_cpu_time": 13822.100000,
                        "fraction_done": 0.773590,
                        "current_cpu_time": 14104.330000,
                        "elapsed_time": 14191.707768,
                        "swap_size": 88653824.000000,
                        "working_set_size": 87760896.000000,
                        "working_set_size_smoothed": 87745446.390313,
                        "page_fault_rate": 0.000000,
                        "bytes_sent": 0.000000,
                        "bytes_received": 0.000000,
                        "progress_rate": 0.000054,
                        "graphics_exec_path": "/var/lib/boinc/projects/www.worldcommunitygrid.org/wcgrid_mcm1_gfx_7.61_x86_64-pc-linux-gnu",
                        "slot_path": "/var/lib/boinc/slots/14",
                    },
                    "project_suspended_via_gui": False,
                },
            ],
        },
    }


@fixture
def screensaver_tasks_multi_result_xml(test_files) -> str:
    return open(f"{test_files}/screensaver_tasks/multi_result.xml").read()


@fixture
def screensaver_tasks_multi_result_dict() -> dict:
    return {
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
                    "ready_to_report": False,
                    "edf_scheduled": False,
                    "active_task": {
                        "active_task_state": 1,
                        "app_version_num": 761,
                        "slot": 14,
                        "pid": 88,
                        "scheduler_state": 2,
                        "checkpoint_cpu_time": 13822.100000,
                        "fraction_done": 0.773590,
                        "current_cpu_time": 14104.330000,
                        "elapsed_time": 14191.707768,
                        "swap_size": 88653824.000000,
                        "working_set_size": 87760896.000000,
                        "working_set_size_smoothed": 87745446.390313,
                        "page_fault_rate": 0.000000,
                        "bytes_sent": 0.000000,
                        "bytes_received": 0.000000,
                        "progress_rate": 0.000054,
                        "graphics_exec_path": "/var/lib/boinc/projects/www.worldcommunitygrid.org/wcgrid_mcm1_gfx_7.61_x86_64-pc-linux-gnu",
                        "slot_path": "/var/lib/boinc/slots/14",
                    },
                    "project_suspended_via_gui": False,
                },
                {
                    "name": "MCM1_0196982_3346_0",
                    "wu_name": "MCM1_0196982_3346",
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
                    "estimated_cpu_time_remaining": 4810.885500,
                    "ready_to_report": False,
                    "edf_scheduled": False,
                    "active_task": {
                        "active_task_state": 1,
                        "app_version_num": 761,
                        "slot": 6,
                        "pid": 91,
                        "scheduler_state": 2,
                        "checkpoint_cpu_time": 12622.800000,
                        "fraction_done": 0.732168,
                        "current_cpu_time": 13085.290000,
                        "elapsed_time": 13151.439764,
                        "swap_size": 87511040.000000,
                        "working_set_size": 86732800.000000,
                        "working_set_size_smoothed": 86718561.740422,
                        "page_fault_rate": 0.000000,
                        "bytes_sent": 0.000000,
                        "bytes_received": 0.000000,
                        "progress_rate": 0.000055,
                        "graphics_exec_path": "/var/lib/boinc/projects/www.worldcommunitygrid.org/wcgrid_mcm1_gfx_7.61_x86_64-pc-linux-gnu",
                        "slot_path": "/var/lib/boinc/slots/6",
                    },
                    "project_suspended_via_gui": False,
                },
            ],
        }
    }


@fixture
def blank_client_state_xml(test_files) -> str:
    return open(f"{test_files}/client_state/no_projects_no_results.xml").read()


@fixture
def blank_client_state_dict() -> dict:
    return {
        "client_state": {
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
                "wsl_available": False,
                "coprocs": [],
            },
            "net_stats": {
                "bwup": 43134.653340,
                "avg_up": 498502.308487,
                "avg_time_up": 1676981888.039070,
                "bwdown": 5198125.722543,
                "avg_down": 936117.076837,
                "avg_time_down": 1676981868.731456,
            },
            "time_stats": {
                "on_frac": 0.375389,
                "connected_frac": -1.000000,
                "cpu_and_network_available_frac": 0.999917,
                "active_frac": 0.999917,
                "gpu_active_frac": 0.999917,
                "client_start_time": 1676897845.254088,
                "total_start_time": 1665649931.082055,
                "total_duration": 2875082.038856,
                "total_active_duration": 2874920.336383,
                "total_gpu_active_duration": 2874920.336383,
                "now": 1676982120.755017,
                "previous_uptime": 19.825332,
                "session_active_duration": 84243.166578,
                "session_gpu_active_duration": 84243.166578,
            },
            "projects": [],
            "apps": [],
            "app_versions": [],
            "work_units": [],
            "results": [],
            "platform_name": "x86_64-pc-linux-gnu",
            "core_client_major_version": 7,
            "core_client_minor_version": 16,
            "core_client_release": 17,
            "executing_as_daemon": False,
            "platform": "x86_64-pc-linux-gnu",
            "global_preferences": {
                "source_project": "",
                "mod_time": 1665411924.000000,
                "battery_charge_min_pct": 90.000000,
                "battery_max_temperature": 40.000000,
                "run_on_batteries": 0,
                "run_if_user_active": 1,
                "run_gpu_if_user_active": 0,
                "suspend_if_no_recent_input": 0.000000,
                "suspend_cpu_usage": 25.000000,
                "start_hour": 0.000000,
                "end_hour": 0.000000,
                "net_start_hour": 0.000000,
                "net_end_hour": 0.000000,
                "leave_apps_in_memory": 0,
                "confirm_before_connecting": 1,
                "hangup_if_dialed": 0,
                "dont_verify_images": 0,
                "work_buf_min_days": 0.100000,
                "work_buf_additional_days": 0.500000,
                "max_ncpus_pct": 50.000000,
                "cpu_scheduling_period_minutes": 60.000000,
                "disk_interval": 180.000000,
                "disk_max_used_gb": 0.000000,
                "disk_max_used_pct": 90.000000,
                "disk_min_free_gb": 1.000000,
                "vm_max_used_pct": 75.000000,
                "ram_max_used_busy_pct": 50.000000,
                "ram_max_used_idle_pct": 90.000000,
                "idle_time_to_run": 3.000000,
                "max_bytes_sec_up": 0.000000,
                "max_bytes_sec_down": 0.000000,
                "cpu_usage_limit": 100.000000,
                "daily_xfer_limit_mb": 0.000000,
                "daily_xfer_period_days": 0,
                "override_file_present": 0,
                "network_wifi_only": 1,
            },
        }
    }


@fixture
def multi_project_no_result_xml(test_files) -> str:
    return open(f"{test_files}/client_state/multi_projects_no_results.xml").read()


@fixture
def multi_project_no_result_dict() -> dict:
    return {
        "client_state": {
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
                "wsl_available": False,
                "coprocs": [],
            },
            "net_stats": {
                "bwup": 43134.653340,
                "avg_up": 498502.308487,
                "avg_time_up": 1676981888.039070,
                "bwdown": 5198125.722543,
                "avg_down": 936117.076837,
                "avg_time_down": 1676981868.731456,
            },
            "time_stats": {
                "on_frac": 0.375389,
                "connected_frac": -1.000000,
                "cpu_and_network_available_frac": 0.999917,
                "active_frac": 0.999917,
                "gpu_active_frac": 0.999917,
                "client_start_time": 1676897845.254088,
                "total_start_time": 1665649931.082055,
                "total_duration": 2875082.038856,
                "total_active_duration": 2874920.336383,
                "total_gpu_active_duration": 2874920.336383,
                "now": 1676982120.755017,
                "previous_uptime": 19.825332,
                "session_active_duration": 84243.166578,
                "session_gpu_active_duration": 84243.166578,
            },
            "apps": [],
            "app_versions": [],
            "work_units": [],
            "results": [],
            "platform_name": "x86_64-pc-linux-gnu",
            "core_client_major_version": 7,
            "core_client_minor_version": 16,
            "core_client_release": 17,
            "executing_as_daemon": False,
            "platform": "x86_64-pc-linux-gnu",
            "projects": [
                {
                    "master_url": "http://www.worldcommunitygrid.org/",
                    "project_name": "World Community Grid",
                    "symstore": "",
                    "user_name": "user_name",
                    "team_name": "",
                    "host_venue": "",
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
                    "dont_use_dcf": False,
                    "dont_request_more_work": False,
                    "master_url_fetch_pending": False,
                    "scheduler_rpc_in_progress": False,
                    "rsc_backoff_time": {"name": "CPU", "value": 0.000000},
                    "rsc_backoff_interval": {"name": "CPU", "value": 0.000000},
                    "gui_urls": [
                        {
                            "name": "Research Overview",
                            "description": "Learn about the projects hosted at World Community Grid",
                            "url": "https://www.worldcommunitygrid.org/research/viewAllProjects.do",
                        }
                    ],
                    "sched_priority": -1.041667,
                    "project_files_downloaded_time": 0.000000,
                    "project_dir": "/var/lib/boinc/projects/www.worldcommunitygrid.org",
                    "suspended_via_gui": False,
                },
                {
                    "master_url": "http://www.spacecommunitygrid.org/",
                    "project_name": "Space Community Grid",
                    "symstore": "",
                    "user_name": "user_name",
                    "team_name": "",
                    "host_venue": "",
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
                    "dont_use_dcf": False,
                    "dont_request_more_work": False,
                    "master_url_fetch_pending": False,
                    "scheduler_rpc_in_progress": False,
                    "rsc_backoff_time": {"name": "CPU", "value": 0.000000},
                    "rsc_backoff_interval": {"name": "CPU", "value": 0.000000},
                    "gui_urls": [
                        {
                            "name": "Research Overview",
                            "description": "Learn about the projects hosted at Space Community Grid",
                            "url": "https://www.spacecommunitygrid.org/research/viewAllProjects.do",
                        }
                    ],
                    "sched_priority": -1.041667,
                    "project_files_downloaded_time": 0.000000,
                    "project_dir": "/var/lib/boinc/projects/www.spacecommunitygrid.org",
                    "suspended_via_gui": False,
                },
            ],
            "global_preferences": {
                "source_project": "",
                "mod_time": 1665411924.000000,
                "battery_charge_min_pct": 90.000000,
                "battery_max_temperature": 40.000000,
                "run_on_batteries": 0,
                "run_if_user_active": 1,
                "run_gpu_if_user_active": 0,
                "suspend_if_no_recent_input": 0.000000,
                "suspend_cpu_usage": 25.000000,
                "start_hour": 0.000000,
                "end_hour": 0.000000,
                "net_start_hour": 0.000000,
                "net_end_hour": 0.000000,
                "leave_apps_in_memory": 0,
                "confirm_before_connecting": 1,
                "hangup_if_dialed": 0,
                "dont_verify_images": 0,
                "work_buf_min_days": 0.100000,
                "work_buf_additional_days": 0.500000,
                "max_ncpus_pct": 50.000000,
                "cpu_scheduling_period_minutes": 60.000000,
                "disk_interval": 180.000000,
                "disk_max_used_gb": 0.000000,
                "disk_max_used_pct": 90.000000,
                "disk_min_free_gb": 1.000000,
                "vm_max_used_pct": 75.000000,
                "ram_max_used_busy_pct": 50.000000,
                "ram_max_used_idle_pct": 90.000000,
                "idle_time_to_run": 3.000000,
                "max_bytes_sec_up": 0.000000,
                "max_bytes_sec_down": 0.000000,
                "cpu_usage_limit": 100.000000,
                "daily_xfer_limit_mb": 0.000000,
                "daily_xfer_period_days": 0,
                "override_file_present": 0,
                "network_wifi_only": 1,
            },
        }
    }


@fixture
def client_state_xml(test_files) -> str:
    return open(f"{test_files}/client_state/short_client_state.xml").read()


@fixture
def client_state_dict() -> dict:
    return {
        "client_state": {
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
                "wsl_available": False,
                "coprocs": [],
            },
            "net_stats": {
                "bwup": 43134.653340,
                "avg_up": 498502.308487,
                "avg_time_up": 1676981888.039070,
                "bwdown": 5198125.722543,
                "avg_down": 936117.076837,
                "avg_time_down": 1676981868.731456,
            },
            "time_stats": {
                "on_frac": 0.375389,
                "connected_frac": -1.000000,
                "cpu_and_network_available_frac": 0.999917,
                "active_frac": 0.999917,
                "gpu_active_frac": 0.999917,
                "client_start_time": 1676897845.254088,
                "total_start_time": 1665649931.082055,
                "total_duration": 2875082.038856,
                "total_active_duration": 2874920.336383,
                "total_gpu_active_duration": 2874920.336383,
                "now": 1676982120.755017,
                "previous_uptime": 19.825332,
                "session_active_duration": 84243.166578,
                "session_gpu_active_duration": 84243.166578,
            },
            "projects": [
                {
                    "master_url": "http://www.worldcommunitygrid.org/",
                    "project_name": "World Community Grid",
                    "symstore": "",
                    "user_name": "user_name",
                    "team_name": "",
                    "host_venue": "",
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
                    "dont_use_dcf": False,
                    "dont_request_more_work": False,
                    "master_url_fetch_pending": False,
                    "scheduler_rpc_in_progress": False,
                    "rsc_backoff_time": {"name": "CPU", "value": 0.000000},
                    "rsc_backoff_interval": {"name": "CPU", "value": 0.000000},
                    "gui_urls": [
                        {
                            "name": "Research Overview",
                            "description": "Learn about the projects hosted at World Community Grid",
                            "url": "https://www.worldcommunitygrid.org/research/viewAllProjects.do",
                        }
                    ],
                    "sched_priority": -1.041667,
                    "project_files_downloaded_time": 0.000000,
                    "project_dir": "/var/lib/boinc/projects/www.worldcommunitygrid.org",
                    "suspended_via_gui": False,
                }
            ],
            "apps": [
                {
                    "name": "opn1",
                    "user_friendly_name": "OpenPandemics - COVID 19",
                    "non_cpu_intensive": False,
                }
            ],
            "app_versions": [
                {
                    "app_name": "opn1",
                    "version_num": 721,
                    "platform": "x86_64-pc-linux-gnu",
                    "avg_ncpus": 1.000000,
                    "flops": 4060616317.600932,
                    "api_version": "7.7.0",
                    "file_ref": [
                        {
                            "file_name": "wcgrid_opn1_autodock_7.21_x86_64-pc-linux-gnu",
                            "main_program": True,
                            "copy_file": False,
                        },
                        {
                            "file_name": "opn1_image09_7.21.tga",
                            "main_program": False,
                            "copy_file": True,
                            "open_name": "Courier.txf",
                        },
                    ],
                }
            ],
            "work_units": [
                {
                    "name": "MCM1_0196931_1689",
                    "app_name": "mcm1",
                    "version_num": 761,
                    "rsc_fpops_est": 31961417063548.000000,
                    "rsc_fpops_bound": 15980708531774000.000000,
                    "rsc_memory_bound": 419430400.000000,
                    "rsc_disk_bound": 524288000.000000,
                    "command_line": "-SettingsFile MCM1_0196931_1689.txt -DatabaseFile dataset-sarc1.txt",
                    "file_ref": [
                        {
                            "file_name": "MCM1_0196931_1689_MCM1_0196931_1689.txt",
                            "open_name": "MCM1_0196931_1689.txt",
                            "main_program": False,
                            "copy_file": False,
                        },
                        {
                            "file_name": "mcm1.dataset-sarc1.txt",
                            "open_name": "dataset-sarc1.txt",
                            "main_program": False,
                            "copy_file": False,
                        },
                    ],
                }
            ],
            "results": [
                {
                    "name": "MCM1_0196931_1633_1",
                    "wu_name": "MCM1_0196931_1633",
                    "platform": "x86_64-pc-linux-gnu",
                    "version_num": 761,
                    "plan_class": None,
                    "project_url": "http://www.worldcommunitygrid.org/",
                    "final_cpu_time": 18111.560000,
                    "final_elapsed_time": 18205.122296,
                    "exit_status": 0,
                    "state": 5,
                    "report_deadline": 1677444048.000000,
                    "received_time": 1676925648.893159,
                    "estimated_cpu_time_remaining": 0.000000,
                    "ready_to_report": True,
                    "edf_scheduled": False,
                    "completed_time": 1676979676.425968,
                    "project_suspended_via_gui": False,
                },
                {
                    "name": "MCM1_0196961_6759_0",
                    "wu_name": "MCM1_0196961_6759",
                    "platform": "x86_64-pc-linux-gnu",
                    "version_num": 761,
                    "plan_class": None,
                    "project_url": "http://www.worldcommunitygrid.org/",
                    "final_cpu_time": 0.000000,
                    "final_elapsed_time": 0.000000,
                    "exit_status": 0,
                    "state": 2,
                    "report_deadline": 1677472761.000000,
                    "received_time": 1676954361.932330,
                    "estimated_cpu_time_remaining": 51.163306,
                    "ready_to_report": False,
                    "edf_scheduled": False,
                    "active_task": {
                        "active_task_state": 1,
                        "app_version_num": 761,
                        "slot": 11,
                        "pid": 337,
                        "scheduler_state": 2,
                        "checkpoint_cpu_time": 17428.570000,
                        "fraction_done": 0.997183,
                        "current_cpu_time": 18025.920000,
                        "elapsed_time": 18113.109104,
                        "swap_size": 94289920.000000,
                        "working_set_size": 93564928.000000,
                        "working_set_size_smoothed": 93551148.758726,
                        "page_fault_rate": 0.000000,
                        "bytes_sent": 0.000000,
                        "bytes_received": 0.000000,
                        "progress_rate": 0.000055,
                        "graphics_exec_path": "/var/lib/boinc/projects/www.worldcommunitygrid.org/wcgrid_mcm1_gfx_7.61_x86_64-pc-linux-gnu",
                        "slot_path": "/var/lib/boinc/slots/11",
                    },
                    "project_suspended_via_gui": False,
                },
            ],
            "platform_name": "x86_64-pc-linux-gnu",
            "core_client_major_version": 7,
            "core_client_minor_version": 16,
            "core_client_release": 17,
            "executing_as_daemon": False,
            "platform": "x86_64-pc-linux-gnu",
            "global_preferences": {
                "source_project": "https://scienceunited.org/",
                "mod_time": 1665411924.000000,
                "battery_charge_min_pct": 90.000000,
                "battery_max_temperature": 40.000000,
                "run_on_batteries": 0,
                "run_if_user_active": 1,
                "run_gpu_if_user_active": 0,
                "suspend_if_no_recent_input": 0.000000,
                "suspend_cpu_usage": 25.000000,
                "start_hour": 0.000000,
                "end_hour": 0.000000,
                "net_start_hour": 0.000000,
                "net_end_hour": 0.000000,
                "leave_apps_in_memory": 1,
                "confirm_before_connecting": 0,
                "hangup_if_dialed": 0,
                "dont_verify_images": 0,
                "work_buf_min_days": 0.100000,
                "work_buf_additional_days": 0.500000,
                "max_ncpus_pct": 50.000000,
                "cpu_scheduling_period_minutes": 60.000000,
                "disk_interval": 180.000000,
                "disk_max_used_gb": 0.000000,
                "disk_max_used_pct": 90.000000,
                "disk_min_free_gb": 1.000000,
                "vm_max_used_pct": 75.000000,
                "ram_max_used_busy_pct": 50.000000,
                "ram_max_used_idle_pct": 90.000000,
                "idle_time_to_run": 3.000000,
                "max_bytes_sec_up": 0.000000,
                "max_bytes_sec_down": 0.000000,
                "cpu_usage_limit": 100.000000,
                "daily_xfer_limit_mb": 0.000000,
                "daily_xfer_period_days": 0,
                "override_file_present": 0,
                "network_wifi_only": 1,
                "max_cpus": 32,
            },
        }
    }


@fixture
def new_project_attach_client_state_xml(test_files) -> str:
    return open(f"{test_files}/client_state/project_attach_weak_key.xml").read()


@fixture
def new_project_attach_client_state_dict() -> dict:
    return {
        "client_state": {
            "host_info": {
                "timezone": 0,
                "domain_name": "boincclient.local",
                "ip_addr": "10.10.10.10",
                "host_cpid": "66ad08359a0d486d9f44edd5ca67422e",
                "p_ncpus": 32,
                "p_vendor": "",
                "p_model": "",
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
                "wsl_available": False,
                "coprocs": [],
            },
            "net_stats": {
                "bwup": 43134.653340,
                "avg_up": 498502.308487,
                "avg_time_up": 1676981888.039070,
                "bwdown": 5198125.722543,
                "avg_down": 936117.076837,
                "avg_time_down": 1676981868.731456,
            },
            "time_stats": {
                "on_frac": 0.375389,
                "connected_frac": -1.000000,
                "cpu_and_network_available_frac": 0.999917,
                "active_frac": 0.999917,
                "gpu_active_frac": 0.999917,
                "client_start_time": 1676897845.254088,
                "total_start_time": 1665649931.082055,
                "total_duration": 2875082.038856,
                "total_active_duration": 2874920.336383,
                "total_gpu_active_duration": 2874920.336383,
                "now": 1676982120.755017,
                "previous_uptime": 19.825332,
                "session_active_duration": 84243.166578,
                "session_gpu_active_duration": 84243.166578,
            },
            "apps": [],
            "app_versions": [],
            "work_units": [],
            "results": [],
            "projects": [
                {
                    "master_url": "https://www.worldcommunitygrid.org/",
                    "project_name": "World Community Grid",
                    "symstore": "",
                    "user_name": "",
                    "team_name": "",
                    "host_venue": "",
                    "email_hash": "",
                    "cross_project_id": "",
                    "external_cpid": "",
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
                    "dont_use_dcf": False,
                    "dont_request_more_work": False,
                    "master_url_fetch_pending": True,
                    "scheduler_rpc_in_progress": True,
                    "rsc_backoff_time": {"name": "CPU", "value": 0.000000},
                    "rsc_backoff_interval": {"name": "CPU", "value": 0.000000},
                    "gui_urls": [],
                    "sched_priority": -1.041667,
                    "project_files_downloaded_time": 0.000000,
                    "project_dir": "/var/lib/boinc/projects/www.worldcommunitygrid.org",
                    "suspended_via_gui": False,
                }
            ],
            "platform_name": "x86_64-pc-linux-gnu",
            "core_client_major_version": 7,
            "core_client_minor_version": 16,
            "core_client_release": 17,
            "executing_as_daemon": False,
            "platform": "x86_64-pc-linux-gnu",
            "global_preferences": {
                "source_project": "",
                "mod_time": 1665411924.000000,
                "battery_charge_min_pct": 90.000000,
                "battery_max_temperature": 40.000000,
                "run_on_batteries": 0,
                "run_if_user_active": 1,
                "run_gpu_if_user_active": 0,
                "suspend_if_no_recent_input": 0.000000,
                "suspend_cpu_usage": 25.000000,
                "start_hour": 0.000000,
                "end_hour": 0.000000,
                "net_start_hour": 0.000000,
                "net_end_hour": 0.000000,
                "leave_apps_in_memory": 1,
                "confirm_before_connecting": 0,
                "hangup_if_dialed": 0,
                "dont_verify_images": 0,
                "work_buf_min_days": 0.100000,
                "work_buf_additional_days": 0.500000,
                "max_ncpus_pct": 50.000000,
                "cpu_scheduling_period_minutes": 60.000000,
                "disk_interval": 180.000000,
                "disk_max_used_gb": 0.000000,
                "disk_max_used_pct": 90.000000,
                "disk_min_free_gb": 1.000000,
                "vm_max_used_pct": 75.000000,
                "ram_max_used_busy_pct": 50.000000,
                "ram_max_used_idle_pct": 90.000000,
                "idle_time_to_run": 3.000000,
                "max_bytes_sec_up": 0.000000,
                "max_bytes_sec_down": 0.000000,
                "cpu_usage_limit": 100.000000,
                "daily_xfer_limit_mb": 0.000000,
                "daily_xfer_period_days": 0,
                "override_file_present": 0,
                "network_wifi_only": 1,
            },
        }
    }


@fixture
def empty_project_status_xml(test_files) -> str:
    return open(f"{test_files}/project_status/no_project.xml").read()


@fixture
def empty_project_status_dict() -> dict:
    return {"project_status": []}


@fixture
def project_status_xml(test_files) -> str:
    return open(f"{test_files}/project_status/single_project.xml").read()


@fixture
def project_status_dict() -> dict:
    return {
        "project_status": [
            {
                "master_url": "http://www.worldcommunitygrid.org/",
                "project_name": "World Community Grid",
                "symstore": "",
                "user_name": "user_name",
                "team_name": "",
                "host_venue": "",
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
                "dont_request_more_work": False,
                "master_url_fetch_pending": False,
                "scheduler_rpc_in_progress": False,
                "rsc_backoff_time": {"name": "CPU", "value": 0.000000},
                "rsc_backoff_interval": {"name": "CPU", "value": 0.000000},
                "gui_urls": [
                    {
                        "name": "Research Overview",
                        "description": "Learn about the projects hosted at World Community Grid",
                        "url": "https://www.worldcommunitygrid.org/research/viewAllProjects.do",
                    },
                    {
                        "name": "News and Updates",
                        "description": "The latest information about World Community Grid and its research projects",
                        "url": "https://www.worldcommunitygrid.org/about_us/displayNews.do",
                    },
                    {
                        "name": "My Contribution",
                        "description": "Your statistics and settings",
                        "url": "https://www.worldcommunitygrid.org/ms/viewMyMemberPage.do",
                    },
                    {
                        "name": "Results Status",
                        "description": "View the status of your assigned work",
                        "url": "https://www.worldcommunitygrid.org/ms/viewBoincResults.do",
                    },
                    {
                        "name": "Device Profiles",
                        "description": "Update your device settings",
                        "url": "https://www.worldcommunitygrid.org/ms/device/viewProfiles.do",
                    },
                    {
                        "name": "Forums",
                        "description": "Visit the World Community Grid forums",
                        "url": "https://www.worldcommunitygrid.org/forumLogin.do",
                    },
                    {
                        "name": "Help",
                        "description": "Search for help in our help system",
                        "url": "https://www.worldcommunitygrid.org/help/viewHelp.do",
                    },
                ],
                "sched_priority": -1.041667,
                "project_files_downloaded_time": 0.000000,
                "project_dir": "/var/lib/boinc/projects/www.worldcommunitygrid.org",
                "suspended_via_gui": False,
                "upload_backoff": 12843.957831,
            }
        ]
    }


@fixture
def no_more_work_project_xml(test_files) -> str:
    return open(f"{test_files}/project_status/no_more_work.xml").read()


@fixture
def no_more_work_project_dict() -> dict:
    return {
        "project_status": [
            {
                "master_url": "http://www.worldcommunitygrid.org/",
                "project_name": "World Community Grid",
                "symstore": "",
                "user_name": "user_name",
                "team_name": "",
                "host_venue": "",
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
                "dont_request_more_work": True,
                "master_url_fetch_pending": False,
                "scheduler_rpc_in_progress": False,
                "rsc_backoff_time": {"name": "CPU", "value": 0.000000},
                "rsc_backoff_interval": {"name": "CPU", "value": 0.000000},
                "gui_urls": [
                    {
                        "name": "Research Overview",
                        "description": "Learn about the projects hosted at World Community Grid",
                        "url": "https://www.worldcommunitygrid.org/research/viewAllProjects.do",
                    },
                    {
                        "name": "News and Updates",
                        "description": "The latest information about World Community Grid and its research projects",
                        "url": "https://www.worldcommunitygrid.org/about_us/displayNews.do",
                    },
                    {
                        "name": "My Contribution",
                        "description": "Your statistics and settings",
                        "url": "https://www.worldcommunitygrid.org/ms/viewMyMemberPage.do",
                    },
                    {
                        "name": "Results Status",
                        "description": "View the status of your assigned work",
                        "url": "https://www.worldcommunitygrid.org/ms/viewBoincResults.do",
                    },
                    {
                        "name": "Device Profiles",
                        "description": "Update your device settings",
                        "url": "https://www.worldcommunitygrid.org/ms/device/viewProfiles.do",
                    },
                    {
                        "name": "Forums",
                        "description": "Visit the World Community Grid forums",
                        "url": "https://www.worldcommunitygrid.org/forumLogin.do",
                    },
                    {
                        "name": "Help",
                        "description": "Search for help in our help system",
                        "url": "https://www.worldcommunitygrid.org/help/viewHelp.do",
                    },
                ],
                "sched_priority": -1.041667,
                "project_files_downloaded_time": 0.000000,
                "project_dir": "/var/lib/boinc/projects/www.worldcommunitygrid.org",
                "suspended_via_gui": False,
                "upload_backoff": 12843.957831,
            }
        ]
    }


@fixture
def suspended_project_status_xml(test_files) -> str:
    return open(f"{test_files}/project_status/suspended_project.xml").read()


@fixture
def suspended_project_status_dict() -> dict:
    return {
        "project_status": [
            {
                "master_url": "http://www.worldcommunitygrid.org/",
                "project_name": "World Community Grid",
                "symstore": "",
                "user_name": "user_name",
                "team_name": "",
                "host_venue": "",
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
                "dont_request_more_work": False,
                "master_url_fetch_pending": False,
                "scheduler_rpc_in_progress": False,
                "rsc_backoff_time": {"name": "CPU", "value": 0.000000},
                "rsc_backoff_interval": {"name": "CPU", "value": 0.000000},
                "gui_urls": [
                    {
                        "name": "Research Overview",
                        "description": "Learn about the projects hosted at World Community Grid",
                        "url": "https://www.worldcommunitygrid.org/research/viewAllProjects.do",
                    }
                ],
                "sched_priority": -1.041667,
                "project_files_downloaded_time": 0.000000,
                "project_dir": "/var/lib/boinc/projects/www.worldcommunitygrid.org",
                "suspended_via_gui": True,
            }
        ]
    }
