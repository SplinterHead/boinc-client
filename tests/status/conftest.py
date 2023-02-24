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
def file_transfers_empty_transfer_xml() -> str:
    return "<file_transfers></file_transfers>"


@fixture
def file_transfers_empty_transfer_dict() -> dict:
    return {"file_transfers": []}


@fixture
def file_transfers_single_transfer_xml() -> str:
    return """<file_transfers>
        <file_transfer>
            <project_url>foo</project_url>
            <project_name>foo</project_name>
            <name>foo</name>
            <nbytes>foo</nbytes>
            <max_nbytes>foo</max_nbytes>
            <status>foo</status>
            <persistent_file_xfer>
                <num_retries>foo</num_retries>
                <first_request_time>foo</first_request_time>
                <next_request_time>foo</next_request_time>
                <time_so_far>foo</time_so_far>
                <last_bytes_xferred>foo</last_bytes_xferred>
                <is_upload>foo</is_upload>
            </persistent_file_xfer>
            <file_xfer>
                <bytes_xferred>foo</bytes_xferred>
                <file_offset>foo</file_offset>
                <xfer_speed>foo</xfer_speed>
                <url>foo</url>
            </file_xfer>
        </file_transfer>
    </file_transfers>"""


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
def file_transfers_multi_transfer_xml() -> str:
    return """<file_transfers>
        <file_transfer>
            <project_url>foo</project_url>
            <project_name>foo</project_name>
            <name>foo</name>
            <nbytes>foo</nbytes>
            <max_nbytes>foo</max_nbytes>
            <status>foo</status>
            <persistent_file_xfer>
                <num_retries>foo</num_retries>
                <first_request_time>foo</first_request_time>
                <next_request_time>foo</next_request_time>
                <time_so_far>foo</time_so_far>
                <last_bytes_xferred>foo</last_bytes_xferred>
                <is_upload>foo</is_upload>
            </persistent_file_xfer>
            <file_xfer>
                <bytes_xferred>foo</bytes_xferred>
                <file_offset>foo</file_offset>
                <xfer_speed>foo</xfer_speed>
                <url>foo</url>
            </file_xfer>
        </file_transfer>
        <file_transfer>
            <project_url>bar</project_url>
            <project_name>bar</project_name>
            <name>bar</name>
            <nbytes>bar</nbytes>
            <max_nbytes>bar</max_nbytes>
            <status>bar</status>
            <persistent_file_xfer>
                <num_retries>bar</num_retries>
                <first_request_time>bar</first_request_time>
                <next_request_time>bar</next_request_time>
                <time_so_far>bar</time_so_far>
                <last_bytes_xferred>bar</last_bytes_xferred>
                <is_upload>bar</is_upload>
            </persistent_file_xfer>
            <file_xfer>
                <bytes_xferred>bar</bytes_xferred>
                <file_offset>bar</file_offset>
                <xfer_speed>bar</xfer_speed>
                <url>bar</url>
            </file_xfer>
        </file_transfer>
    </file_transfers>"""


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
def simple_gui_info_empty_xml() -> str:
    return "<simple_gui_info></simple_gui_info>"


@fixture
def simple_gui_info_empty_dict() -> dict:
    return {"gui_info": {"projects": [], "results": []}}


@fixture
def simple_gui_info_singles_xml() -> str:
    return """<simple_gui_info>
    <project>
        <master_url>foo</master_url>
        <project_name>foo</project_name>
        <symstore>foo</symstore>
        <user_name>foo</user_name>
        <team_name>foo</team_name>
        <host_venue>foo</host_venue>
        <email_hash>foo</email_hash>
        <cross_project_id>foo</cross_project_id>
        <external_cpid>foo</external_cpid>
        <cpid_time>foo</cpid_time>
        <user_total_credit>foo</user_total_credit>
        <user_expavg_credit>foo</user_expavg_credit>
        <user_create_time>foo</user_create_time>
        <rpc_seqno>foo</rpc_seqno>
        <userid>foo</userid>
        <teamid>foo</teamid>
        <hostid>foo</hostid>
        <host_total_credit>foo</host_total_credit>
        <host_expavg_credit>foo</host_expavg_credit>
        <host_create_time>foo</host_create_time>
        <nrpc_failures>foo</nrpc_failures>
        <master_fetch_failures>foo</master_fetch_failures>
        <min_rpc_time>foo</min_rpc_time>
        <next_rpc_time>foo</next_rpc_time>
        <rec>foo</rec>
        <rec_time>foo</rec_time>
        <resource_share>foo</resource_share>
        <disk_usage>foo</disk_usage>
        <disk_share>foo</disk_share>
        <desired_disk_usage>foo</desired_disk_usage>
        <duration_correction_factor>foo</duration_correction_factor>
        <sched_rpc_pending>foo</sched_rpc_pending>
        <send_time_stats_log>foo</send_time_stats_log>
        <send_job_log>foo</send_job_log>
        <njobs_success>foo</njobs_success>
        <njobs_error>foo</njobs_error>
        <elapsed_time>foo</elapsed_time>
        <last_rpc_time>foo</last_rpc_time>
        <dont_use_dcf>foo</dont_use_dcf>
        <rsc_backoff_time>
            <name>CPU</name>
            <value>0.000000</value>
        </rsc_backoff_time>
        <rsc_backoff_interval>
            <name>CPU</name>
            <value>0.000000</value>
        </rsc_backoff_interval>
        <gui_urls>
            <gui_url>
              <name>Foo 1</name>
              <description>foo</description>
              <url>foo</url>
            </gui_url>
            <gui_url>
              <name>Foo 2</name>
              <description>foo</description>
              <url>foo</url>
            </gui_url>
        </gui_urls>
        <sched_priority>foo</sched_priority>
        <project_files_downloaded_time>foo</project_files_downloaded_time>
        <project_dir>foo</project_dir>
    </project>
    <result>
        <name>foo</name>
        <wu_name>foo</wu_name>
        <platform>foo</platform>
        <version_num>foo</version_num>
        <plan_class>foo</plan_class>
        <project_url>foo</project_url>
        <final_cpu_time>foo</final_cpu_time>
        <final_elapsed_time>foo</final_elapsed_time>
        <exit_status>foo</exit_status>
        <state>foo</state>
        <report_deadline>foo</report_deadline>
        <received_time>foo</received_time>
        <estimated_cpu_time_remaining>foo</estimated_cpu_time_remaining>
        <active_task>
            <active_task_state>foo</active_task_state>
            <app_version_num>foo</app_version_num>
            <slot>foo</slot>
            <pid>foo</pid>
            <scheduler_state>foo</scheduler_state>
            <checkpoint_cpu_time>foo</checkpoint_cpu_time>
            <fraction_done>foo</fraction_done>
            <current_cpu_time>foo</current_cpu_time>
            <elapsed_time>foo</elapsed_time>
            <swap_size>foo</swap_size>
            <working_set_size>foo</working_set_size>
            <working_set_size_smoothed>foo</working_set_size_smoothed>
            <page_fault_rate>foo</page_fault_rate>
            <bytes_sent>foo</bytes_sent>
            <bytes_received>foo</bytes_received>
            <progress_rate>foo</progress_rate>
            <graphics_exec_path>foo</graphics_exec_path>
            <slot_path>foo</slot_path>
        </active_task>
    </result>
</simple_gui_info>"""


@fixture
def simple_gui_info_singles_dict() -> dict:
    return {
        "gui_info": {
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
                    "rsc_backoff_time": {"name": "CPU", "value": "0.000000"},
                    "rsc_backoff_interval": {"name": "CPU", "value": "0.000000"},
                    "gui_urls": [
                        {"name": "Foo 1", "description": "foo", "url": "foo"},
                        {"name": "Foo 2", "description": "foo", "url": "foo"},
                    ],
                    "sched_priority": "foo",
                    "project_files_downloaded_time": "foo",
                    "project_dir": "foo",
                }
            ],
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
                        "progress_rate": "foo",
                        "graphics_exec_path": "foo",
                        "slot_path": "foo",
                    },
                }
            ],
        }
    }


@fixture
def simple_gui_info_multi_xml() -> str:
    return """<simple_gui_info>
    <project>
        <master_url>foo</master_url>
        <project_name>foo</project_name>
        <symstore>foo</symstore>
        <user_name>foo</user_name>
        <team_name>foo</team_name>
        <host_venue>foo</host_venue>
        <email_hash>foo</email_hash>
        <cross_project_id>foo</cross_project_id>
        <external_cpid>foo</external_cpid>
        <cpid_time>foo</cpid_time>
        <user_total_credit>foo</user_total_credit>
        <user_expavg_credit>foo</user_expavg_credit>
        <user_create_time>foo</user_create_time>
        <rpc_seqno>foo</rpc_seqno>
        <userid>foo</userid>
        <teamid>foo</teamid>
        <hostid>foo</hostid>
        <host_total_credit>foo</host_total_credit>
        <host_expavg_credit>foo</host_expavg_credit>
        <host_create_time>foo</host_create_time>
        <nrpc_failures>foo</nrpc_failures>
        <master_fetch_failures>foo</master_fetch_failures>
        <min_rpc_time>foo</min_rpc_time>
        <next_rpc_time>foo</next_rpc_time>
        <rec>foo</rec>
        <rec_time>foo</rec_time>
        <resource_share>foo</resource_share>
        <disk_usage>foo</disk_usage>
        <disk_share>foo</disk_share>
        <desired_disk_usage>foo</desired_disk_usage>
        <duration_correction_factor>foo</duration_correction_factor>
        <sched_rpc_pending>foo</sched_rpc_pending>
        <send_time_stats_log>foo</send_time_stats_log>
        <send_job_log>foo</send_job_log>
        <njobs_success>foo</njobs_success>
        <njobs_error>foo</njobs_error>
        <elapsed_time>foo</elapsed_time>
        <last_rpc_time>foo</last_rpc_time>
        <dont_use_dcf>foo</dont_use_dcf>
        <rsc_backoff_time>
            <name>CPU</name>
            <value>0.000000</value>
        </rsc_backoff_time>
        <rsc_backoff_interval>
            <name>CPU</name>
            <value>0.000000</value>
        </rsc_backoff_interval>
        <gui_urls>
            <gui_url>
              <name>Foo 1</name>
              <description>foo</description>
              <url>foo</url>
            </gui_url>
            <gui_url>
              <name>Foo 2</name>
              <description>foo</description>
              <url>foo</url>
            </gui_url>
        </gui_urls>
        <sched_priority>foo</sched_priority>
        <project_files_downloaded_time>foo</project_files_downloaded_time>
        <project_dir>foo</project_dir>
    </project>
    <project>
        <master_url>bar</master_url>
        <project_name>bar</project_name>
        <symstore>bar</symstore>
        <user_name>bar</user_name>
        <team_name>bar</team_name>
        <host_venue>bar</host_venue>
        <email_hash>bar</email_hash>
        <cross_project_id>bar</cross_project_id>
        <external_cpid>bar</external_cpid>
        <cpid_time>bar</cpid_time>
        <user_total_credit>bar</user_total_credit>
        <user_expavg_credit>bar</user_expavg_credit>
        <user_create_time>bar</user_create_time>
        <rpc_seqno>bar</rpc_seqno>
        <userid>bar</userid>
        <teamid>bar</teamid>
        <hostid>bar</hostid>
        <host_total_credit>bar</host_total_credit>
        <host_expavg_credit>bar</host_expavg_credit>
        <host_create_time>bar</host_create_time>
        <nrpc_failures>bar</nrpc_failures>
        <master_fetch_failures>bar</master_fetch_failures>
        <min_rpc_time>bar</min_rpc_time>
        <next_rpc_time>bar</next_rpc_time>
        <rec>bar</rec>
        <rec_time>bar</rec_time>
        <resource_share>bar</resource_share>
        <disk_usage>bar</disk_usage>
        <disk_share>bar</disk_share>
        <desired_disk_usage>bar</desired_disk_usage>
        <duration_correction_factor>bar</duration_correction_factor>
        <sched_rpc_pending>bar</sched_rpc_pending>
        <send_time_stats_log>bar</send_time_stats_log>
        <send_job_log>bar</send_job_log>
        <njobs_success>bar</njobs_success>
        <njobs_error>bar</njobs_error>
        <elapsed_time>bar</elapsed_time>
        <last_rpc_time>bar</last_rpc_time>
        <dont_use_dcf>foo</dont_use_dcf>
        <rsc_backoff_time>
            <name>CPU</name>
            <value>0.000000</value>
        </rsc_backoff_time>
        <rsc_backoff_interval>
            <name>CPU</name>
            <value>0.000000</value>
        </rsc_backoff_interval>
        <gui_urls>
            <gui_url>
              <name>Bar 1</name>
              <description>bar</description>
              <url>bar</url>
            </gui_url>
            <gui_url>
              <name>Foo 2</name>
              <description>bar</description>
              <url>bar</url>
            </gui_url>
        </gui_urls>
        <sched_priority>bar</sched_priority>
        <project_files_downloaded_time>bar</project_files_downloaded_time>
        <project_dir>bar</project_dir>
    </project>
    <result>
        <name>foo</name>
        <wu_name>foo</wu_name>
        <platform>foo</platform>
        <version_num>foo</version_num>
        <plan_class>foo</plan_class>
        <project_url>foo</project_url>
        <final_cpu_time>foo</final_cpu_time>
        <final_elapsed_time>foo</final_elapsed_time>
        <exit_status>foo</exit_status>
        <state>foo</state>
        <report_deadline>foo</report_deadline>
        <received_time>foo</received_time>
        <estimated_cpu_time_remaining>foo</estimated_cpu_time_remaining>
        <active_task>
            <active_task_state>foo</active_task_state>
            <app_version_num>foo</app_version_num>
            <slot>foo</slot>
            <pid>foo</pid>
            <scheduler_state>foo</scheduler_state>
            <checkpoint_cpu_time>foo</checkpoint_cpu_time>
            <fraction_done>foo</fraction_done>
            <current_cpu_time>foo</current_cpu_time>
            <elapsed_time>foo</elapsed_time>
            <swap_size>foo</swap_size>
            <working_set_size>foo</working_set_size>
            <working_set_size_smoothed>foo</working_set_size_smoothed>
            <page_fault_rate>foo</page_fault_rate>
            <bytes_sent>foo</bytes_sent>
            <bytes_received>foo</bytes_received>
            <progress_rate>foo</progress_rate>
            <graphics_exec_path>foo</graphics_exec_path>
            <slot_path>foo</slot_path>
        </active_task>
    </result>
    <result>
        <name>bar</name>
        <wu_name>bar</wu_name>
        <platform>bar</platform>
        <version_num>bar</version_num>
        <plan_class>bar</plan_class>
        <project_url>bar</project_url>
        <final_cpu_time>bar</final_cpu_time>
        <final_elapsed_time>bar</final_elapsed_time>
        <exit_status>bar</exit_status>
        <state>bar</state>
        <report_deadline>bar</report_deadline>
        <received_time>bar</received_time>
        <estimated_cpu_time_remaining>bar</estimated_cpu_time_remaining>
        <active_task>
            <active_task_state>bar</active_task_state>
            <app_version_num>bar</app_version_num>
            <slot>bar</slot>
            <pid>bar</pid>
            <scheduler_state>bar</scheduler_state>
            <checkpoint_cpu_time>bar</checkpoint_cpu_time>
            <fraction_done>bar</fraction_done>
            <current_cpu_time>bar</current_cpu_time>
            <elapsed_time>bar</elapsed_time>
            <swap_size>bar</swap_size>
            <working_set_size>bar</working_set_size>
            <working_set_size_smoothed>bar</working_set_size_smoothed>
            <page_fault_rate>bar</page_fault_rate>
            <bytes_sent>bar</bytes_sent>
            <bytes_received>bar</bytes_received>
            <progress_rate>bar</progress_rate>
            <graphics_exec_path>bar</graphics_exec_path>
            <slot_path>bar</slot_path>
        </active_task>
    </result>
</simple_gui_info>"""


@fixture
def simple_gui_info_multi_dict() -> dict:
    return {
        "gui_info": {
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
                    "rsc_backoff_time": {"name": "CPU", "value": "0.000000"},
                    "rsc_backoff_interval": {"name": "CPU", "value": "0.000000"},
                    "gui_urls": [
                        {"name": "Foo 1", "description": "foo", "url": "foo"},
                        {"name": "Foo 2", "description": "foo", "url": "foo"},
                    ],
                    "sched_priority": "foo",
                    "project_files_downloaded_time": "foo",
                    "project_dir": "foo",
                },
                {
                    "master_url": "bar",
                    "project_name": "bar",
                    "symstore": "bar",
                    "user_name": "bar",
                    "team_name": "bar",
                    "host_venue": "bar",
                    "email_hash": "bar",
                    "cross_project_id": "bar",
                    "external_cpid": "bar",
                    "cpid_time": "bar",
                    "user_total_credit": "bar",
                    "user_expavg_credit": "bar",
                    "user_create_time": "bar",
                    "rpc_seqno": "bar",
                    "userid": "bar",
                    "teamid": "bar",
                    "hostid": "bar",
                    "host_total_credit": "bar",
                    "host_expavg_credit": "bar",
                    "host_create_time": "bar",
                    "nrpc_failures": "bar",
                    "master_fetch_failures": "bar",
                    "min_rpc_time": "bar",
                    "next_rpc_time": "bar",
                    "rec": "bar",
                    "rec_time": "bar",
                    "resource_share": "bar",
                    "disk_usage": "bar",
                    "disk_share": "bar",
                    "desired_disk_usage": "bar",
                    "duration_correction_factor": "bar",
                    "sched_rpc_pending": "bar",
                    "send_time_stats_log": "bar",
                    "send_job_log": "bar",
                    "njobs_success": "bar",
                    "njobs_error": "bar",
                    "elapsed_time": "bar",
                    "last_rpc_time": "bar",
                    "dont_use_dcf": "foo",
                    "rsc_backoff_time": {"name": "CPU", "value": "0.000000"},
                    "rsc_backoff_interval": {"name": "CPU", "value": "0.000000"},
                    "gui_urls": [
                        {"name": "Bar 1", "description": "bar", "url": "bar"},
                        {"name": "Foo 2", "description": "bar", "url": "bar"},
                    ],
                    "sched_priority": "bar",
                    "project_files_downloaded_time": "bar",
                    "project_dir": "bar",
                },
            ],
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
                        "progress_rate": "foo",
                        "graphics_exec_path": "foo",
                        "slot_path": "foo",
                    },
                },
                {
                    "name": "bar",
                    "wu_name": "bar",
                    "platform": "bar",
                    "version_num": "bar",
                    "plan_class": "bar",
                    "project_url": "bar",
                    "final_cpu_time": "bar",
                    "final_elapsed_time": "bar",
                    "exit_status": "bar",
                    "state": "bar",
                    "report_deadline": "bar",
                    "received_time": "bar",
                    "estimated_cpu_time_remaining": "bar",
                    "active_task": {
                        "active_task_state": "bar",
                        "app_version_num": "bar",
                        "slot": "bar",
                        "pid": "bar",
                        "scheduler_state": "bar",
                        "checkpoint_cpu_time": "bar",
                        "fraction_done": "bar",
                        "current_cpu_time": "bar",
                        "elapsed_time": "bar",
                        "swap_size": "bar",
                        "working_set_size": "bar",
                        "working_set_size_smoothed": "bar",
                        "page_fault_rate": "bar",
                        "bytes_sent": "bar",
                        "bytes_received": "bar",
                        "progress_rate": "bar",
                        "graphics_exec_path": "bar",
                        "slot_path": "bar",
                    },
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
                },
            ],
        }
    }


@fixture
def client_state_xml() -> str:
    return """<client_state>
    <host_info>
        <timezone>foo</timezone>
        <domain_name>foo</domain_name>
        <ip_addr>foo</ip_addr>
        <host_cpid>foo</host_cpid>
        <p_ncpus>foo</p_ncpus>
        <p_vendor>foo</p_vendor>
        <p_model>foo</p_model>
        <p_features>foo</p_features>
        <p_fpops>foo</p_fpops>
        <p_iops>foo</p_iops>
        <p_membw>foo</p_membw>
        <p_calculated>foo</p_calculated>
        <p_vm_extensions_disabled>foo</p_vm_extensions_disabled>
        <m_nbytes>foo</m_nbytes>
        <m_cache>foo</m_cache>
        <m_swap>foo</m_swap>
        <d_total>foo</d_total>
        <d_free>foo</d_free>
        <os_name>foo</os_name>
        <os_version>foo</os_version>
        <n_usable_coprocs>foo</n_usable_coprocs>
        <wsl_available>foo</wsl_available>
    </host_info>
    <net_stats>
        <bwup>foo</bwup>
        <avg_up>foo</avg_up>
        <avg_time_up>foo</avg_time_up>
        <bwdown>foo</bwdown>
        <avg_down>foo</avg_down>
        <avg_time_down>foo</avg_time_down>
    </net_stats>
    <time_stats>
        <on_frac>foo</on_frac>
        <connected_frac>foo</connected_frac>
        <cpu_and_network_available_frac>foo</cpu_and_network_available_frac>
        <active_frac>foo</active_frac>
        <gpu_active_frac>foo</gpu_active_frac>
        <client_start_time>foo</client_start_time>
        <total_start_time>foo</total_start_time>
        <total_duration>foo</total_duration>
        <total_active_duration>foo</total_active_duration>
        <total_gpu_active_duration>foo</total_gpu_active_duration>
        <now>foo</now>
        <previous_uptime>foo</previous_uptime>
        <session_active_duration>foo</session_active_duration>
        <session_gpu_active_duration>foo</session_gpu_active_duration>
    </time_stats>
    <platform_name>foo</platform_name>
    <core_client_major_version>foo</core_client_major_version>
    <core_client_minor_version>foo</core_client_minor_version>
    <core_client_release>foo</core_client_release>
    <executing_as_daemon>foo</executing_as_daemon>
    <platform>foo</platform>
    <global_preferences>
       <source_project>foo</source_project>
       <mod_time>foo</mod_time>
       <battery_charge_min_pct>foo</battery_charge_min_pct>
       <battery_max_temperature>foo</battery_max_temperature>
       <run_on_batteries>foo</run_on_batteries>
       <run_if_user_active>foo</run_if_user_active>
       <run_gpu_if_user_active>foo</run_gpu_if_user_active>
       <suspend_if_no_recent_input>foo</suspend_if_no_recent_input>
       <suspend_cpu_usage>foo</suspend_cpu_usage>
       <start_hour>foo</start_hour>
       <end_hour>foo</end_hour>
       <net_start_hour>foo</net_start_hour>
       <net_end_hour>foo</net_end_hour>
       <leave_apps_in_memory>foo</leave_apps_in_memory>
       <confirm_before_connecting>foo</confirm_before_connecting>
       <hangup_if_dialed>foo</hangup_if_dialed>
       <dont_verify_images>foo</dont_verify_images>
       <work_buf_min_days>foo</work_buf_min_days>
       <work_buf_additional_days>foo</work_buf_additional_days>
       <max_ncpus_pct>foo</max_ncpus_pct>
       <cpu_scheduling_period_minutes>foo</cpu_scheduling_period_minutes>
       <disk_interval>foo</disk_interval>
       <disk_max_used_gb>foo</disk_max_used_gb>
       <disk_max_used_pct>foo</disk_max_used_pct>
       <disk_min_free_gb>foo</disk_min_free_gb>
       <vm_max_used_pct>foo</vm_max_used_pct>
       <ram_max_used_busy_pct>foo</ram_max_used_busy_pct>
       <ram_max_used_idle_pct>foo</ram_max_used_idle_pct>
       <idle_time_to_run>foo</idle_time_to_run>
       <max_bytes_sec_up>foo</max_bytes_sec_up>
       <max_bytes_sec_down>foo</max_bytes_sec_down>
       <cpu_usage_limit>foo</cpu_usage_limit>
       <daily_xfer_limit_mb>foo</daily_xfer_limit_mb>
       <daily_xfer_period_days>foo</daily_xfer_period_days>
       <override_file_present>foo</override_file_present>
       <network_wifi_only>foo</network_wifi_only>
    </global_preferences>
</client_state>"""


@fixture
def client_state_dict() -> dict:
    return {
        "client_state": {
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
                "n_usable_coprocs": "foo",
                "wsl_available": "foo",
            },
            "net_stats": {
                "bwup": "foo",
                "avg_up": "foo",
                "avg_time_up": "foo",
                "bwdown": "foo",
                "avg_down": "foo",
                "avg_time_down": "foo",
            },
            "time_stats": {
                "on_frac": "foo",
                "connected_frac": "foo",
                "cpu_and_network_available_frac": "foo",
                "active_frac": "foo",
                "gpu_active_frac": "foo",
                "client_start_time": "foo",
                "total_start_time": "foo",
                "total_duration": "foo",
                "total_active_duration": "foo",
                "total_gpu_active_duration": "foo",
                "now": "foo",
                "previous_uptime": "foo",
                "session_active_duration": "foo",
                "session_gpu_active_duration": "foo",
            },
            "platform_name": "foo",
            "core_client_major_version": "foo",
            "core_client_minor_version": "foo",
            "core_client_release": "foo",
            "executing_as_daemon": "foo",
            "platform": "foo",
            "global_preferences": {
                "source_project": "foo",
                "mod_time": "foo",
                "battery_charge_min_pct": "foo",
                "battery_max_temperature": "foo",
                "run_on_batteries": "foo",
                "run_if_user_active": "foo",
                "run_gpu_if_user_active": "foo",
                "suspend_if_no_recent_input": "foo",
                "suspend_cpu_usage": "foo",
                "start_hour": "foo",
                "end_hour": "foo",
                "net_start_hour": "foo",
                "net_end_hour": "foo",
                "leave_apps_in_memory": "foo",
                "confirm_before_connecting": "foo",
                "hangup_if_dialed": "foo",
                "dont_verify_images": "foo",
                "work_buf_min_days": "foo",
                "work_buf_additional_days": "foo",
                "max_ncpus_pct": "foo",
                "cpu_scheduling_period_minutes": "foo",
                "disk_interval": "foo",
                "disk_max_used_gb": "foo",
                "disk_max_used_pct": "foo",
                "disk_min_free_gb": "foo",
                "vm_max_used_pct": "foo",
                "ram_max_used_busy_pct": "foo",
                "ram_max_used_idle_pct": "foo",
                "idle_time_to_run": "foo",
                "max_bytes_sec_up": "foo",
                "max_bytes_sec_down": "foo",
                "cpu_usage_limit": "foo",
                "daily_xfer_limit_mb": "foo",
                "daily_xfer_period_days": "foo",
                "override_file_present": "foo",
                "network_wifi_only": "foo",
            },
        }
    }


@fixture
def empty_project_state_xml() -> str:
    return "<projects></projects>"


@fixture
def empty_project_state_dict() -> dict:
    return {"project_states": []}


@fixture
def project_state_xml(test_files) -> str:
    return open(f"{test_files}/project_state/single_project.xml").read()


@fixture
def project_state_dict() -> dict:
    return {
        "project_states": [
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
            }
        ]
    }
