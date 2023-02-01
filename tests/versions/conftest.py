from pytest import fixture


@fixture
def server_version_xml() -> str:
    return """<server_version>
        <major>1</major>
        <minor>2</minor>
        <release>0</release>
    </server_version>"""


@fixture
def server_version_dict() -> dict:
    return {"major": "1", "minor": "2", "release": "0"}


@fixture
def server_update_xml() -> str:
    return """<newer_version>1.3.0</newer_version>
        <download_url>http://boincclientdownload.info/v1_3_0.exe</download_url>"""


@fixture
def server_update_dict() -> dict:
    return {
        "update": {
            "newer_version": "1.3.0",
            "download_url": "http://boincclientdownload.info/v1_3_0.exe",
        }
    }
