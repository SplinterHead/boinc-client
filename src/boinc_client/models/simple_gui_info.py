from marshmallow import Schema, fields, pre_load

from boinc_client.models.project_status import ProjectState
from boinc_client.models.result import Result


class GuiInfo(Schema):
    projects = fields.Nested(ProjectState(many=True), data_key="project")
    results = fields.Nested(Result(many=True), data_key="result")


class SimpleGuiInfo(Schema):
    gui_info = fields.Nested(GuiInfo(), data_key="simple_gui_info")

    @pre_load
    def _a_normalise_none(self, data, **kwargs):
        if not data["simple_gui_info"]:
            data["simple_gui_info"] = {"project": [], "result": []}
        return data
