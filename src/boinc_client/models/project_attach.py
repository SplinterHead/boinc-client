from marshmallow import Schema, fields, pre_load


class ProjectAttach(Schema):
    success = fields.Bool()
    error = fields.Str(allow_none=True)

    @pre_load
    def _fill_success(self, data, **kwargs):
        data["success"] = "success" in data
        return data


class ProjectAttachPollMessages(Schema):
    messages = fields.List(fields.Str(), allow_none=True, data_key="message")
    error_num = fields.Int()


class ProjectAttachPoll(Schema):
    project_attach_reply = fields.Nested(ProjectAttachPollMessages())
