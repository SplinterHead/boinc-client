from pytest import fixture


@fixture
def global_prefs_xml(test_files) -> str:
    return open(f"{test_files}/global_preferences/global_prefs.xml").read()


@fixture
def global_prefs_dict(test_files) -> dict:
    return {
        "global_preferences": {
            "battery_charge_min_pct": 90.000000,
            "battery_max_temperature": 40.000000,
            "confirm_before_connecting": 0,
            "cpu_scheduling_period_minutes": 120.000000,
            "cpu_usage_limit": 60.000000,
            "daily_xfer_limit_mb": 0.000000,
            "daily_xfer_period_days": 0,
            "disk_interval": 60.000000,
            "disk_max_used_gb": 10.000000,
            "disk_max_used_pct": 50.000000,
            "disk_min_free_gb": 0.500000,
            "dont_verify_images": 0,
            "end_hour": 0.000000,
            "hangup_if_dialed": 0,
            "idle_time_to_run": 3.000000,
            "leave_apps_in_memory": 1,
            "max_bytes_sec_down": 0.000000,
            "max_bytes_sec_up": 0.000000,
            "max_cpus": 32,
            "max_ncpus_pct": 100.000000,
            "mod_time": 1665410370.000000,
            "net_end_hour": 0.000000,
            "net_start_hour": 0.000000,
            "network_wifi_only": 1,
            "override_file_present": 0,
            "ram_max_used_busy_pct": 50.000000,
            "ram_max_used_idle_pct": 75.000000,
            "run_gpu_if_user_active": 0,
            "run_if_user_active": 1,
            "run_on_batteries": 0,
            "source_project": "https://www.worldcommunitygrid.org/",
            "start_hour": 0.000000,
            "suspend_cpu_usage": 50.000000,
            "suspend_if_no_recent_input": 0.000000,
            "vm_max_used_pct": 50.000000,
            "work_buf_additional_days": 0.300000,
            "work_buf_min_days": 0.200000,
        }
    }


@fixture
def global_prefs_override_xml(test_files) -> str:
    return open(f"{test_files}/global_preferences/global_prefs_override.xml").read()


@fixture
def global_prefs_override_dict(test_files) -> dict:
    return {
        "global_preferences": {
            "confirm_before_connecting": 1,
            "cpu_scheduling_period_minutes": 60.000000,
            "cpu_usage_limit": 50.000000,
            "daily_xfer_limit_mb": 0.000000,
            "daily_xfer_period_days": 0,
            "disk_interval": 60.000000,
            "disk_max_used_gb": 0.000000,
            "disk_max_used_pct": 90.000000,
            "disk_min_free_gb": 0.100000,
            "dont_verify_images": 0,
            "end_hour": 0.000000,
            "hangup_if_dialed": 0,
            "idle_time_to_run": 3.000000,
            "leave_apps_in_memory": 0,
            "max_bytes_sec_down": 0.000000,
            "max_bytes_sec_up": 0.000000,
            "max_ncpus_pct": 20.000000,
            "net_end_hour": 0.000000,
            "net_start_hour": 0.000000,
            "ram_max_used_busy_pct": 50.000000,
            "ram_max_used_idle_pct": 90.000000,
            "run_gpu_if_user_active": 0,
            "run_if_user_active": 1,
            "run_on_batteries": 0,
            "start_hour": 0.000000,
            "suspend_cpu_usage": 25.000000,
            "suspend_if_no_recent_input": 0.000000,
            "vm_max_used_pct": 75.000000,
            "work_buf_additional_days": 0.500000,
            "work_buf_min_days": 0.100000,
        }
    }
