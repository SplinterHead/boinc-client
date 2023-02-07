import json

from pydantic import Field
from pytest import mark

from pyboinc.models.client_update import ClientUpdate
from pyboinc.models.client_version import ClientVersion


@mark.model
def test_client_version_model_can_parse_dict(server_version_dict):
    test_json = {"server_version": {"major": "1", "minor": "2", "release": "0"}}
    test_model = ClientVersion.parse_obj(test_json)

    assert test_model
    assert test_model.dict() == server_version_dict
    assert test_model.sem_ver() == "v1.2.0"


@mark.model
def test_client_update_model_can_parse_dict(server_update_json, server_update_dict):
    test_model = ClientUpdate.parse_obj(server_update_json)

    assert test_model
    assert test_model.dict() == server_update_dict
