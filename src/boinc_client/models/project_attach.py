from marshmallow import Schema, fields


class ProjectAttachPollMessages(Schema):
    messages = fields.List(fields.Str(), allow_none=True, data_key="message")
    error_num = fields.Int()


class ProjectAttachPoll(Schema):
    project_attach_reply = fields.Nested(ProjectAttachPollMessages())
