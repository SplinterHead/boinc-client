from pytest import fixture


@fixture
def empty_network_transfer_report_xml(test_files) -> str:
    return open(f"{test_files}/network_transfers/empty_network_transfers.xml").read()


@fixture
def empty_network_transfer_report_dict() -> dict:
    return {"network_transfers": {}}


@fixture
def daily_network_transfer_report_xml(test_files) -> str:
    return open(f"{test_files}/network_transfers/single_network_transfer.xml").read()


@fixture
def daily_network_transfer_report_dict() -> dict:
    return {"network_transfers": {"2023-01-01": {"up": 1000.000, "down": 6000.000}}}


@fixture
def multi_daily_network_transfer_report_xml(test_files) -> str:
    return open(f"{test_files}/network_transfers/multiple_network_transfers.xml").read()


@fixture
def multi_daily_network_transfer_report_dict() -> dict:
    return {
        "network_transfers": {
            "2023-01-01": {"up": 1000.000, "down": 6000.000},
            "2023-01-02": {"up": 2000.000, "down": 5000.000},
        }
    }


@fixture
def empty_project_stats_xml(test_files) -> str:
    return open(f"{test_files}/project_stats/empty_project_stats.xml").read()


@fixture
def empty_project_stats_dict() -> dict:
    return {"project_stats": []}


@fixture
def single_project_single_day_stats_xml(test_files) -> str:
    return open(
        f"{test_files}/project_stats/single_project_single_day_stats.xml"
    ).read()


@fixture
def single_project_single_day_stats_dict() -> dict:
    return {
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


@fixture
def single_project_multi_day_stats_xml(test_files) -> str:
    return open(f"{test_files}/project_stats/single_project_multi_day_stats.xml").read()


@fixture
def single_project_multi_day_stats_dict() -> dict:
    return {
        "project_stats": [
            {
                "master_url": "http://www.worldcommunitygrid.org/",
                "daily_statistics": {
                    "2023-01-22": {
                        "user_total_credit": 252425.687796,
                        "user_expavg_credit": 1433.823904,
                        "host_total_credit": 251023.015252,
                        "host_expavg_credit": 1428.390798,
                    },
                    "2023-01-23": {
                        "user_total_credit": 256712.775099,
                        "user_expavg_credit": 1754.946077,
                        "host_total_credit": 255310.102555,
                        "host_expavg_credit": 1749.852530,
                    },
                },
            }
        ]
    }


@fixture
def multi_project_single_day_stats_xml(test_files) -> str:
    return open(f"{test_files}/project_stats/multi_project_single_day_stats.xml").read()


@fixture
def multi_project_single_day_stats_dict() -> dict:
    return {
        "project_stats": [
            {
                "master_url": "http://www.worldcommunitygrid.org/",
                "daily_statistics": {
                    "2023-01-22": {
                        "user_total_credit": 252425.687796,
                        "user_expavg_credit": 1433.823904,
                        "host_total_credit": 251023.015252,
                        "host_expavg_credit": 1428.390798,
                    },
                },
            },
            {
                "master_url": "http://www.spacecommunitygrid.org/",
                "daily_statistics": {
                    "2023-02-15": {
                        "user_total_credit": 252425.687796,
                        "user_expavg_credit": 1433.823904,
                        "host_total_credit": 251023.015252,
                        "host_expavg_credit": 1428.390798,
                    }
                },
            },
        ]
    }
