from pytest import fixture


@fixture
def basic_cc_status_xml() -> str:
    return """<cc_status>
        <network_status>2</network_status>
        <ams_password_error>0</ams_password_error>
        <task_suspend_reason>0</task_suspend_reason>
        <task_mode>2</task_mode>
        <task_mode_perm>2</task_mode_perm>
        <task_mode_delay>0.000000</task_mode_delay>
        <gpu_suspend_reason>0</gpu_suspend_reason>
        <gpu_mode>2</gpu_mode>
        <gpu_mode_perm>2</gpu_mode_perm>
        <gpu_mode_delay>0.000000</gpu_mode_delay>
        <network_suspend_reason>0</network_suspend_reason>
        <network_mode>2</network_mode>
        <network_mode_perm>2</network_mode_perm>
        <network_mode_delay>0.000000</network_mode_delay>
        <disallow_attach>0</disallow_attach>
        <simple_gui_only>0</simple_gui_only>
        <max_event_log_lines>2000</max_event_log_lines>
    </cc_status>"""


@fixture
def basic_cc_status_dict() -> dict:
    return {
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
            "max_event_log_lines": "2000",
        }
    }


@fixture
def disk_stats_no_project_xml() -> str:
    return """<disk_usage_summary>
        <d_total>100</d_total>
        <d_free>20</d_free>
        <d_boinc>50</d_boinc>
        <d_allowed>75</d_allowed>
    </disk_usage_summary>"""


@fixture
def disk_stats_no_project_dict() -> dict:
    return {
        "disk_stats": {
            "projects": [],
            "d_total": "100",
            "d_free": "20",
            "d_boinc": "50",
            "d_allowed": "75",
        }
    }


@fixture
def disk_stats_single_project_xml() -> str:
    return """<disk_usage_summary>
        <project>
            <master_url>https://projecta.com</master_url>
            <disk_usage>30</disk_usage>
        </project>
        <d_total>100</d_total>
        <d_free>20</d_free>
        <d_boinc>50</d_boinc>
        <d_allowed>75</d_allowed>
    </disk_usage_summary>"""


@fixture
def disk_stats_single_project_dict() -> dict:
    return {
        "disk_stats": {
            "projects": [{"master_url": "https://projecta.com", "disk_usage": "30"}],
            "d_total": "100",
            "d_free": "20",
            "d_boinc": "50",
            "d_allowed": "75",
        }
    }


@fixture
def disk_stats_multi_project_xml() -> str:
    return """<disk_usage_summary>
        <project>
            <master_url>https://projecta.com</master_url>
            <disk_usage>30</disk_usage>
        </project>
        <project>
            <master_url>https://projectb.com</master_url>
            <disk_usage>35</disk_usage>
        </project>
        <d_total>100</d_total>
        <d_free>20</d_free>
        <d_boinc>50</d_boinc>
        <d_allowed>75</d_allowed>
    </disk_usage_summary>"""


@fixture
def disk_stats_multi_project_dict() -> dict:
    return {
        "disk_stats": {
            "projects": [
                {"master_url": "https://projecta.com", "disk_usage": "30"},
                {"master_url": "https://projectb.com", "disk_usage": "35"},
            ],
            "d_total": "100",
            "d_free": "20",
            "d_boinc": "50",
            "d_allowed": "75",
        }
    }


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
def host_info_xml() -> str:
    return """<host_info>
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
        <product_name>foo</product_name>
        <virtualbox_version>foo</virtualbox_version>
        <coprocs>
            <coproc_intel_gpu>
                <count>foo</count>
                <name>foo</name>
                <available_ram>foo</available_ram>
                <have_opencl>foo</have_opencl>
                <peak_flops>foo</peak_flops>
                <version>foo</version>
                <coproc_opencl>
                    <name>foo</name>
                    <vendor>foo</vendor>
                    <vendor_id>foo</vendor_id>
                    <available>foo</available>
                    <half_fp_config>foo</half_fp_config>
                    <single_fp_config>foo</single_fp_config>
                    <double_fp_config>foo</double_fp_config>
                    <endian_little>foo</endian_little>
                    <execution_capabilities>foo</execution_capabilities>
                    <extensions>foo</extensions>
                    <global_mem_size>foo</global_mem_size>
                    <local_mem_size>foo</local_mem_size>
                    <max_clock_frequency>foo</max_clock_frequency>
                    <max_compute_units>foo</max_compute_units>
                    <nv_compute_capability_major>foo</nv_compute_capability_major>
                    <nv_compute_capability_minor>foo</nv_compute_capability_minor>
                    <amd_simd_per_compute_unit>foo</amd_simd_per_compute_unit>
                    <amd_simd_width>foo</amd_simd_width>
                    <amd_simd_instruction_width>foo</amd_simd_instruction_width>
                    <opencl_platform_version>foo</opencl_platform_version>
                    <opencl_device_version>foo</opencl_device_version>
                    <opencl_driver_version>foo</opencl_driver_version>
                </coproc_opencl>
            </coproc_intel_gpu>
        </coprocs>
        <opencl_cpu_prop>
            <platform_vendor>foo</platform_vendor>
            <opencl_cpu_info>
                <name>foo</name>
                <vendor>foo</vendor>
                <vendor_id>foo</vendor_id>
                <available>foo</available>
                <half_fp_config>foo</half_fp_config>
                <single_fp_config>foo</single_fp_config>
                <double_fp_config>foo</double_fp_config>
                <endian_little>foo</endian_little>
                <execution_capabilities>foo</execution_capabilities>
                <extensions>foo</extensions>
                <global_mem_size>foo</global_mem_size>
                <local_mem_size>foo</local_mem_size>
                <max_clock_frequency>foo</max_clock_frequency>
                <max_compute_units>foo</max_compute_units>
                <nv_compute_capability_major>foo</nv_compute_capability_major>
                <nv_compute_capability_minor>foo</nv_compute_capability_minor>
                <amd_simd_per_compute_unit>foo</amd_simd_per_compute_unit>
                <amd_simd_width>foo</amd_simd_width>
                <amd_simd_instruction_width>foo</amd_simd_instruction_width>
                <opencl_platform_version>foo</opencl_platform_version>
                <opencl_device_version>foo</opencl_device_version>
                <opencl_driver_version>foo</opencl_driver_version>
            </opencl_cpu_info>
        </opencl_cpu_prop>
    </host_info>"""


@fixture
def host_info_dict() -> dict:
    return {
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
                "coproc_intel_gpu": {
                    "count": "foo",
                    "name": "foo",
                    "available_ram": "foo",
                    "have_opencl": "foo",
                    "peak_flops": "foo",
                    "version": "foo",
                    "coproc_opencl": {
                        "name": "foo",
                        "vendor": "foo",
                        "vendor_id": "foo",
                        "available": "foo",
                        "half_fp_config": "foo",
                        "single_fp_config": "foo",
                        "double_fp_config": "foo",
                        "endian_little": "foo",
                        "execution_capabilities": "foo",
                        "extensions": "foo",
                        "global_mem_size": "foo",
                        "local_mem_size": "foo",
                        "max_clock_frequency": "foo",
                        "max_compute_units": "foo",
                        "nv_compute_capability_major": "foo",
                        "nv_compute_capability_minor": "foo",
                        "amd_simd_per_compute_unit": "foo",
                        "amd_simd_width": "foo",
                        "amd_simd_instruction_width": "foo",
                        "opencl_platform_version": "foo",
                        "opencl_device_version": "foo",
                        "opencl_driver_version": "foo",
                    },
                }
            },
            "opencl_cpu_prop": {
                "platform_vendor": "foo",
                "opencl_cpu_info": {
                    "name": "foo",
                    "vendor": "foo",
                    "vendor_id": "foo",
                    "available": "foo",
                    "half_fp_config": "foo",
                    "single_fp_config": "foo",
                    "double_fp_config": "foo",
                    "endian_little": "foo",
                    "execution_capabilities": "foo",
                    "extensions": "foo",
                    "global_mem_size": "foo",
                    "local_mem_size": "foo",
                    "max_clock_frequency": "foo",
                    "max_compute_units": "foo",
                    "nv_compute_capability_major": "foo",
                    "nv_compute_capability_minor": "foo",
                    "amd_simd_per_compute_unit": "foo",
                    "amd_simd_width": "foo",
                    "amd_simd_instruction_width": "foo",
                    "opencl_platform_version": "foo",
                    "opencl_device_version": "foo",
                    "opencl_driver_version": "foo",
                },
            },
        }
    }
