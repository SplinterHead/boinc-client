from marshmallow import Schema, fields, post_load, pre_load


class NoticeContent(Schema):
    title = fields.Str()
    description = fields.Str()
    create_time = fields.Int()
    arrival_time = fields.Int()
    is_private = fields.Bool()
    project_name = fields.Str()
    category = fields.Str()
    link = fields.Url()
    seqno = fields.Int()

    @post_load
    def _remove_seqno(self, data, **kwargs):
        del data["seqno"]
        return data


class Notices(Schema):
    notices = fields.Dict(fields.Int(), fields.Nested(NoticeContent()))

    @pre_load
    def _convert_none_to_empty_dict(self, data, **kwargs):
        data["notices"] = {} if not data["notices"] else data["notices"]["notice"]
        return data

    @pre_load
    def _create_dict_keys(self, data, **kwargs):
        data["notices"] = {m["seqno"]: m for m in data["notices"]}
        return data
