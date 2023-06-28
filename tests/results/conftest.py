from pytest import fixture


@fixture
def empty_result_xml(test_files) -> str:
    return open(f"{test_files}/results/empty_results.xml").read()


@fixture
def empty_result_dict() -> dict:
    return {"results": []}


@fixture
def single_pending_result_xml(test_files) -> str:
    return open(f"{test_files}/results/single_pending_result.xml").read()


@fixture
def single_pending_result_dict() -> dict:
    return {
        "results": [
            {
                "name": "MCM1_0196917_7759_0",
                "wu_name": "MCM1_0196917_7759",
                "platform": "x86_64-pc-linux-gnu",
                "version_num": 761,
                "plan_class": None,
                "project_url": "http://www.worldcommunitygrid.org/",
                "final_cpu_time": 0.000000,
                "final_elapsed_time": 0.000000,
                "exit_status": 0,
                "state": 2,
                "report_deadline": 1677416632.000000,
                "received_time": 1676898233.328302,
                "estimated_cpu_time_remaining": 15050.234471,
                "ready_to_report": False,
                "edf_scheduled": False,
                "project_suspended_via_gui": False,
            }
        ]
    }


@fixture
def single_suspended_result_xml(test_files) -> str:
    return open(f"{test_files}/results/single_suspended_result.xml").read()


@fixture
def single_suspended_result_dict() -> dict:
    return {
        "results": [
            {
                "name": "MCM1_0196917_7759_0",
                "wu_name": "MCM1_0196917_7759",
                "platform": "x86_64-pc-linux-gnu",
                "version_num": 761,
                "plan_class": None,
                "project_url": "http://www.worldcommunitygrid.org/",
                "final_cpu_time": 0.000000,
                "final_elapsed_time": 0.000000,
                "exit_status": 0,
                "state": 2,
                "report_deadline": 1677416632.000000,
                "received_time": 1676898233.328302,
                "estimated_cpu_time_remaining": 15050.234471,
                "ready_to_report": False,
                "edf_scheduled": False,
                "project_suspended_via_gui": True,
            }
        ]
    }


@fixture
def single_active_result_xml(test_files) -> str:
    return open(f"{test_files}/results/single_active_result.xml").read()


@fixture
def single_active_result_dict() -> dict:
    return {
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
        ]
    }


@fixture
def single_completed_result_xml(test_files) -> str:
    return open(f"{test_files}/results/single_completed_result.xml").read()


@fixture
def single_completed_result_dict() -> dict:
    return {
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
                "completed_time": 1676979676.425968,
                "edf_scheduled": False,
                "project_suspended_via_gui": False,
            }
        ]
    }


@fixture
def multi_result_xml(test_files) -> str:
    return open(f"{test_files}/results/multiple_results.xml").read()


@fixture
def multi_result_dict() -> dict:
    return {
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
                "edf_scheduled": False,
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
            },
            {
                "name": "MCM1_0196917_7759_0",
                "wu_name": "MCM1_0196917_7759",
                "platform": "x86_64-pc-linux-gnu",
                "version_num": 761,
                "plan_class": None,
                "project_url": "http://www.worldcommunitygrid.org/",
                "final_cpu_time": 0.000000,
                "final_elapsed_time": 0.000000,
                "exit_status": 0,
                "state": 2,
                "report_deadline": 1677416632.000000,
                "received_time": 1676898233.328302,
                "estimated_cpu_time_remaining": 15050.234471,
                "ready_to_report": False,
                "edf_scheduled": False,
                "project_suspended_via_gui": False,
            },
        ]
    }


@fixture
def empty_old_result_xml(test_files) -> str:
    return open(f"{test_files}/old_results/empty_old_results.xml").read()


@fixture
def empty_old_result_dict() -> dict:
    return {"old_results": []}


@fixture
def single_old_result_xml(test_files) -> str:
    return open(f"{test_files}/old_results/single_old_result.xml").read()


@fixture
def single_old_result_dict() -> dict:
    return {
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


@fixture
def multi_old_result_xml(test_files) -> str:
    return open(f"{test_files}/old_results/multiple_old_results.xml").read()


@fixture
def multi_old_result_dict() -> dict:
    return {
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
            },
            {
                "project_url": "http://www.worldcommunitygrid.org/",
                "result_name": "MCM1_0196482_6936_1",
                "app_name": "mcm1",
                "exit_status": 0,
                "elapsed_time": 18663.505252,
                "cpu_time": 18533.470000,
                "completed_time": 1676908636.814082,
                "create_time": 1676908642.830881,
            },
        ]
    }
