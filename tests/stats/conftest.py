from pytest import fixture


@fixture
def empty_network_transfer_report_xml() -> str:
    return "<daily_xfers></daily_xfers>"


@fixture
def empty_network_transfer_report_dict() -> dict:
    return {"network_stats": {}}


@fixture
def daily_network_transfer_report_xml() -> str:
    return """<daily_xfers>
        <dx>
            <when>19358</when>
            <up>1000.000</up>
            <down>6000.000</down>
        </dx>
    </daily_xfers>"""


@fixture
def daily_network_transfer_report_dict() -> dict:
    return {"network_stats": {"2023-01-01": {"up": 1000.000, "down": 6000.000}}}


@fixture
def multi_daily_network_transfer_report_xml() -> str:
    return """<daily_xfers>
        <dx>
            <when>19358</when>
            <up>1000.000</up>
            <down>6000.000</down>
        </dx>
        <dx>
            <when>19359</when>
            <up>2000.000</up>
            <down>5000.000</down>
        </dx>
    </daily_xfers>"""


@fixture
def multi_daily_network_transfer_report_dict() -> dict:
    return {
        "network_stats": {
            "2023-01-01": {"up": 1000.000, "down": 6000.000},
            "2023-01-02": {"up": 2000.000, "down": 5000.000},
        }
    }


@fixture
def single_project_single_day_stats_xml() -> str:
    return """<statistics>
        <project_statistics>
            <master_url>foo_url</master_url>
            <daily_statistics>
                <day>foo_day</day>
                <user_total_credit>foo</user_total_credit>
                <user_expavg_credit>foo</user_expavg_credit>
                <host_total_credit>foo</host_total_credit>
                <host_expavg_credit>foo</host_expavg_credit>
            </daily_statistics>
        </project_statistics>
    </statistics>"""


@fixture
def single_project_single_day_stats_dict() -> dict:
    return {
        "project_stats": [
            {
                "master_url": "foo_url",
                "daily_statistics": {
                    "foo_day": {
                        "user_total_credit": "foo",
                        "user_expavg_credit": "foo",
                        "host_total_credit": "foo",
                        "host_expavg_credit": "foo",
                    }
                },
            }
        ]
    }


@fixture
def single_project_multi_day_stats_xml() -> str:
    return """<statistics>
        <project_statistics>
            <master_url>foo_url</master_url>
            <daily_statistics>
                <day>foo_day</day>
                <user_total_credit>foo</user_total_credit>
                <user_expavg_credit>foo</user_expavg_credit>
                <host_total_credit>foo</host_total_credit>
                <host_expavg_credit>foo</host_expavg_credit>
            </daily_statistics>
            <daily_statistics>
                <day>bar_day</day>
                <user_total_credit>bar</user_total_credit>
                <user_expavg_credit>bar</user_expavg_credit>
                <host_total_credit>bar</host_total_credit>
                <host_expavg_credit>bar</host_expavg_credit>
            </daily_statistics>
        </project_statistics>
    </statistics>"""


@fixture
def single_project_multi_day_stats_dict() -> dict:
    return {
        "project_stats": [
            {
                "master_url": "foo_url",
                "daily_statistics": {
                    "foo_day": {
                        "user_total_credit": "foo",
                        "user_expavg_credit": "foo",
                        "host_total_credit": "foo",
                        "host_expavg_credit": "foo",
                    },
                    "bar_day": {
                        "user_total_credit": "bar",
                        "user_expavg_credit": "bar",
                        "host_total_credit": "bar",
                        "host_expavg_credit": "bar",
                    },
                },
            }
        ]
    }


@fixture
def multi_project_single_day_stats_xml() -> str:
    return """<statistics>
        <project_statistics>
            <master_url>foo_url</master_url>
            <daily_statistics>
                <day>foo_day</day>
                <user_total_credit>foo</user_total_credit>
                <user_expavg_credit>foo</user_expavg_credit>
                <host_total_credit>foo</host_total_credit>
                <host_expavg_credit>foo</host_expavg_credit>
            </daily_statistics>
        </project_statistics>
        <project_statistics>
            <master_url>bar_url</master_url>
            <daily_statistics>
                <day>bar_day</day>
                <user_total_credit>bar</user_total_credit>
                <user_expavg_credit>bar</user_expavg_credit>
                <host_total_credit>bar</host_total_credit>
                <host_expavg_credit>bar</host_expavg_credit>
            </daily_statistics>
        </project_statistics>
    </statistics>"""


@fixture
def multi_project_single_day_stats_dict() -> dict:
    return {
        "project_stats": [
            {
                "master_url": "foo_url",
                "daily_statistics": {
                    "foo_day": {
                        "user_total_credit": "foo",
                        "user_expavg_credit": "foo",
                        "host_total_credit": "foo",
                        "host_expavg_credit": "foo",
                    }
                },
            },
            {
                "master_url": "bar_url",
                "daily_statistics": {
                    "bar_day": {
                        "user_total_credit": "bar",
                        "user_expavg_credit": "bar",
                        "host_total_credit": "bar",
                        "host_expavg_credit": "bar",
                    }
                },
            },
        ]
    }
