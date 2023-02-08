from pytest import mark


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
    assert result is not {}


# Messages
@mark.integration
def test_messages(boinc_client):
    result = boinc_client.get_messages()
    assert result
    assert result is not {}
