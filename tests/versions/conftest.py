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
