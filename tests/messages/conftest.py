from pytest import fixture


@fixture
def single_messages_xml(test_files) -> str:
    return open(f"{test_files}/messages/single_message.xml").read()


@fixture
def single_messages_dict(test_files) -> dict:
    return {
        "messages": {
            109: {
                "project": "World Community Grid",
                "pri": "1",
                "body": "Finished download of MCM1_FILENAME.txt",
                "time": 1676897897,
            }
        }
    }


@fixture
def none_proj_messages_xml(test_files) -> str:
    return open(f"{test_files}/messages/single_message_with_nones.xml").read()


@fixture
def none_proj_messages_dict() -> dict:
    return {
        "messages": {
            64: {
                "project": None,
                "pri": "1",
                "body": None,
                "time": 1676897876,
            }
        }
    }


@fixture
def multi_messages_xml(test_files) -> str:
    return open(f"{test_files}/messages/multi_messages.xml").read()


@fixture
def multi_messages_dict() -> dict:
    return {
        "messages": {
            109: {
                "project": "World Community Grid",
                "pri": "1",
                "body": "Finished download of MCM1_FILENAME.txt",
                "time": 1676897897,
            },
            110: {
                "project": "World Community Grid",
                "pri": "1",
                "body": "Started download of MCM2_FILENAME.txt",
                "time": 1676897897,
            },
        }
    }


@fixture
def empty_notice_xml(test_files) -> str:
    return open(f"{test_files}/notices/empty_notice.xml").read()


@fixture
def empty_notice_dict() -> dict:
    return {"notices": {}}


@fixture
def single_notice_xml(test_files) -> str:
    return open(f"{test_files}/notices/single_notice.xml").read()


@fixture
def single_notice_dict() -> dict:
    return {
        "notices": {
            1: {
                "title": "Notice A",
                "description": "This is a notice",
                "create_time": 123,
                "arrival_time": 124,
                "is_private": False,
                "project_name": "proja",
                "category": "test",
                "link": "https://linky.link",
            }
        }
    }


@fixture
def nulled_notice_xml(test_files) -> str:
    return open(f"{test_files}/notices/nulled_notice.xml").read()


@fixture
def nulled_notice_dict() -> dict:
    return {
        "notices": {
            1: {
                "title": None,
                "description": "This is a notice",
                "create_time": 1688708837.806547,
                "arrival_time": 1688708837.806547,
                "is_private": False,
                "project_name": "proja",
                "category": "client",
                "link": None,
            }
        }
    }


@fixture
def multi_notice_xml(test_files) -> str:
    return open(f"{test_files}/notices/multi_notices.xml").read()


@fixture
def multi_notice_dict() -> dict:
    return {
        "notices": {
            1: {
                "title": "Notice A",
                "description": "This is a notice",
                "create_time": 123,
                "arrival_time": 124,
                "is_private": False,
                "project_name": "proja",
                "category": "test",
                "link": "https://linky.link",
            },
            2: {
                "title": "Notice B",
                "description": "This is another notice",
                "create_time": 456,
                "arrival_time": 457,
                "is_private": False,
                "project_name": "projb",
                "category": "test2",
                "link": "https://linky2.link",
            },
        }
    }
