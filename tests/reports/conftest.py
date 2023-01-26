from pytest import fixture


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
