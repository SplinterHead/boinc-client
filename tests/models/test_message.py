from boinc_client.models.message import Messages


def test_message_model_can_parse_single():
    test_dict = {
        "msgs": {
            "msg": [
                {
                    "project": "Project A",
                    "pri": "proja",
                    "seqno": "1",
                    "body": "This is a Message",
                    "time": "1672531200",
                }
            ]
        }
    }

    expected_dict = {
        "messages": {
            1: {
                "project": "Project A",
                "pri": "proja",
                "body": "This is a Message",
                "time": 1672531200,
            }
        }
    }

    model = Messages().load(test_dict)
    assert model == expected_dict


def test_message_model_can_parse_multiple():
    test_dict = {
        "msgs": {
            "msg": [
                {
                    "project": "Project A",
                    "pri": "proja",
                    "seqno": "1",
                    "body": "This is a Message",
                    "time": "1672531200",
                },
                {
                    "project": "Project B",
                    "pri": "projb",
                    "seqno": "2",
                    "body": "This is a Message",
                    "time": "1672531300",
                },
            ]
        }
    }

    expected_dict = {
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
                "body": "This is a Message",
                "time": 1672531300,
            },
        }
    }

    model = Messages().load(test_dict)
    assert model == expected_dict
