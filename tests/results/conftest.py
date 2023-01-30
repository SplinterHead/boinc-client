from pytest import fixture


@fixture
def single_result_xml() -> str:
    return """<results>
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
        <project_suspended_via_gui>foo</project_suspended_via_gui>
        <report_immediately>foo</report_immediately>
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
        </active_task>
        <resources>foo</resources>
    </result>
</results>"""


@fixture
def single_result_dict() -> dict:
    return {
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
                    "progress_rate": "foo",
                },
                "resources": "foo",
            }
        ]
    }


@fixture
def multi_result_xml() -> str:
    return """<results>
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
        <project_suspended_via_gui>foo</project_suspended_via_gui>
        <report_immediately>foo</report_immediately>
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
        </active_task>
        <resources>foo</resources>
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
        <project_suspended_via_gui>bar</project_suspended_via_gui>
        <report_immediately>bar</report_immediately>
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
        </active_task>
        <resources>bar</resources>
    </result>
</results>"""


@fixture
def multi_result_dict() -> dict:
    return {
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
                    "progress_rate": "foo",
                },
                "resources": "foo",
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
                "project_suspended_via_gui": "bar",
                "report_immediately": "bar",
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
                },
                "resources": "bar",
            },
        ]
    }


@fixture
def single_old_result_xml() -> str:
    return """<old_results>
        <old_result>
            <project_url>foo</project_url>
            <result_name>foo</result_name>
            <app_name>foo</app_name>
            <exit_status>foo</exit_status>
            <elapsed_time>foo</elapsed_time>
            <cpu_time>foo</cpu_time>
            <completed_time>foo</completed_time>
            <create_time>foo</create_time>
        </old_result>
    </old_results>"""


@fixture
def single_old_result_dict() -> dict:
    return {
        "old_results": [
            {
                "project_url": "foo",
                "result_name": "foo",
                "app_name": "foo",
                "exit_status": "foo",
                "elapsed_time": "foo",
                "cpu_time": "foo",
                "completed_time": "foo",
                "create_time": "foo",
            }
        ]
    }


@fixture
def multi_old_result_xml() -> str:
    return """<old_results>
        <old_result>
            <project_url>foo</project_url>
            <result_name>foo</result_name>
            <app_name>foo</app_name>
            <exit_status>foo</exit_status>
            <elapsed_time>foo</elapsed_time>
            <cpu_time>foo</cpu_time>
            <completed_time>foo</completed_time>
            <create_time>foo</create_time>
        </old_result>
        <old_result>
            <project_url>bar</project_url>
            <result_name>bar</result_name>
            <app_name>bar</app_name>
            <exit_status>bar</exit_status>
            <elapsed_time>bar</elapsed_time>
            <cpu_time>bar</cpu_time>
            <completed_time>bar</completed_time>
            <create_time>bar</create_time>
        </old_result>
    </old_results>"""


@fixture
def multi_old_result_dict() -> dict:
    return {
        "old_results": [
            {
                "project_url": "foo",
                "result_name": "foo",
                "app_name": "foo",
                "exit_status": "foo",
                "elapsed_time": "foo",
                "cpu_time": "foo",
                "completed_time": "foo",
                "create_time": "foo",
            },
            {
                "project_url": "bar",
                "result_name": "bar",
                "app_name": "bar",
                "exit_status": "bar",
                "elapsed_time": "bar",
                "cpu_time": "bar",
                "completed_time": "bar",
                "create_time": "bar",
            },
        ]
    }
