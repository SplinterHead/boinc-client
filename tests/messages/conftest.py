from pytest import fixture


@fixture
def single_messages_xml(test_files) -> str:
    return open(f"{test_files}/messages/single_message.xml").read()


@fixture
def single_messages_dict(test_files) -> dict:
    return {
        "messages": {
            1: {
                "project": "Project A",
                "pri": "proja",
                "body": "This is a Message",
                "time": 1672531200,
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
            1: {
                "project": None,
                "pri": "proja",
                "body": None,
                "time": 1672531200,
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
            1: {
                "project": "Project A",
                "pri": "proja",
                "body": "This is a Message",
                "time": 1672531200,
            },
            2: {
                "project": "Project B",
                "pri": "projb",
                "body": "This is another Message",
                "time": 1672531300,
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
