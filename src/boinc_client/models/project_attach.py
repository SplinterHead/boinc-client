from marshmallow import Schema, fields


class ProjectAttachPollMessages(Schema):
    error_num = fields.Int()
    messages = fields.List(fields.Str(), allow_none=True, data_key="message")


class ProjectAttachPoll(Schema):
    project_attach_reply = fields.Nested(ProjectAttachPollMessages())
