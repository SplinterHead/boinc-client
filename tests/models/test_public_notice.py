from boinc_client.models.public_notice import Notices


def test_notice_model_can_parse_empty():
    test_dict = {"notices": None}

    expected_dict = {"notices": {}}

    model = Notices().load(test_dict)
    assert model == expected_dict


def test_notice_model_can_parse_single():
    test_dict = {
        "notices": {
            "notice": [
                {
                    "title": "Notice A",
                    "description": "This is a notice",
                    "create_time": "123",
                    "arrival_time": "124",
                    "is_private": "false",
                    "project_name": "proja",
                    "category": "test",
                    "link": "https://linky.link",
                    "seqno": "1",
                }
            ]
        }
    }

    expected_dict = {
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

    model = Notices().load(test_dict)
    assert model == expected_dict


def test_notice_model_can_parse_multiple():
    test_dict = {
        "notices": {
            "notice": [
                {
                    "title": "Notice A",
                    "description": "This is a notice",
                    "create_time": "123",
                    "arrival_time": "124",
                    "is_private": "false",
                    "project_name": "proja",
                    "category": "test",
                    "link": "https://linky.link",
                    "seqno": "1",
                },
                {
                    "title": "Notice B",
                    "description": "This is a notice",
                    "create_time": "126",
                    "arrival_time": "127",
                    "is_private": "false",
                    "project_name": "projb",
                    "category": "test",
                    "link": "https://linky.link",
                    "seqno": "2",
                },
            ]
        }
    }

    expected_dict = {
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
                "description": "This is a notice",
                "create_time": 126,
                "arrival_time": 127,
                "is_private": False,
                "project_name": "projb",
                "category": "test",
                "link": "https://linky.link",
            },
        }
    }

    model = Notices().load(test_dict)
    assert model == expected_dict
