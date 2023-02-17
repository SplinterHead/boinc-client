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
@mark.integration
def test_results(boinc_client):
    result = boinc_client.get_results()
    assert result
    assert "results" in result


@mark.integration
def test_old_results(boinc_client):
    result = boinc_client.get_old_results()
    assert result
    assert "old_results" in result


# Stats
@mark.integration
def test_network_stats(boinc_client):
    result = boinc_client.get_network_stats()
    assert result
    assert "network_stats" in result


@mark.integration
def test_project_stats(boinc_client):
    result = boinc_client.get_project_stats()
    assert result
    assert "project_stats" in result


# Status
@mark.integration
def test_client_state(boinc_client):
    result = boinc_client.get_client_state()
    assert result
    assert "client_state" in result


# Status
@mark.integration
def test_project_state(boinc_client):
    result = boinc_client.get_project_state()
    assert result
    assert "projects" in result


# Status
@mark.integration
def test_cc_state(boinc_client):
    result = boinc_client.get_cc_status()
    assert result
    assert "cc_status" in result


# Status
@mark.integration
def test_disk_stats(boinc_client):
    result = boinc_client.get_disk_stats()
    assert result
    assert "disk_stats" in result


# Status
@mark.integration
def test_file_transfers(boinc_client):
    result = boinc_client.get_file_transfers()
    assert result
    assert "file_transfers" in result


# Status
@mark.integration
def test_host_info(boinc_client):
    result = boinc_client.get_host_info()
    assert result
    assert "host_info" in result


# Status
@mark.integration
def test_simple_gui_info(boinc_client):
    result = boinc_client.get_simple_gui_info()
    assert result
    assert "gui_info" in result


# Status
@mark.integration
def test_screensaver_tasks(boinc_client):
    result = boinc_client.get_screensaver_tasks()
    assert result
    assert "screensaver_tasks" in result


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
