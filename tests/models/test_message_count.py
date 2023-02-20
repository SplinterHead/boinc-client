from boinc_client.models.message_count import MessageCount


def test_message_count_model_can_parse():
    test_dict = {"seqno": "2"}

    expected_dict = {"message_count": 2}

    model = MessageCount().load(test_dict)
    assert model == expected_dict
