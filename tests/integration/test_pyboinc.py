import pytest


@pytest.mark.integration
def test_container_version(boinc_client):
    assert boinc_client.client_version()


# @pytest.mark.integration
# def test_get_all_projects(boinc_client):
#     assert boinc_client.get_all_projects()

@pytest.mark.integration
def test_messages(boinc_client):
    assert boinc_client.get_messages()
