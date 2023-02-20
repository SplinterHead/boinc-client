from pytest import fixture


@fixture
def server_version_xml(test_files) -> str:
    return open(f"{test_files}/versions/server_version.xml").read()


@fixture
def server_version_dict(test_files) -> dict:
    return {
        "version": {
            "major": 1, "minor": 2, "patch": 0
        }
    }


@fixture
def server_update_xml(test_files) -> str:
    return open(f"{test_files}/versions/server_update.xml").read()


@fixture
def server_update_dict(test_files) -> dict:
    return {
        "update": {
            "newer_version": "1.3.0",
            "download_url": "https://boinc.berkeley.edu/download.php"
        }
    }


@fixture
def server_update_no_xml(test_files) -> str:
    return open(f"{test_files}/versions/server_no_update.xml").read()


@fixture
def server_update_no_dict(test_files) -> dict:
    return {
        "update": {
            "newer_version": None,
            "download_url": "https://boinc.berkeley.edu/download.php"
        }
    }
