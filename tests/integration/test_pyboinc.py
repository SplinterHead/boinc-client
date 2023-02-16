from pytest import mark


# Messages
@mark.integration
def test_messages(boinc_client):
    result = boinc_client.get_messages()
    assert result
    assert "messages" in result


@mark.integration
def test_message_with_start(boinc_client):
    all_msg = boinc_client.get_messages()
    result = boinc_client.get_messages(start=1)
    assert result
    assert "messages" in result
    assert len(result["messages"]) == len(all_msg["messages"]) - 1


@mark.integration
def test_message_count(boinc_client):
    result = boinc_client.get_message_count()
    assert result
    assert "message_count" in result


@mark.integration
def test_public_notices(boinc_client):
    result = boinc_client.get_public_notices()
    assert result
    assert "notices" in result


# Projects
@mark.integration
def test_all_projects_list(boinc_client):
    result = boinc_client.get_all_projects()
    assert result
    assert "projects" in result


# Results
# @mark.integration
# def test_results(boinc_client):
#     result = boinc_client.get_results()
#     assert result


# Versions
@mark.integration
def test_container_version(boinc_client):
    result = boinc_client.get_client_version()
    assert result
    assert result is not {}


@mark.integration
def test_container_update(boinc_client):
    result = boinc_client.get_client_update()
    assert result
    assert "update" in result


# Messages
@mark.integration
def test_messages(boinc_client):
    result = boinc_client.get_messages()
    assert result
    assert result is not {}
