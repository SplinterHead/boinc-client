from marshmallow import Schema, fields, post_load, pre_load

from boinc_client.models.helpers import (
    create_indexes,
    flatten_data,
    normalise_none_to_list,
    remove_key,
)


class Notice(Schema):
    title = fields.Str(allow_none=True)
    description = fields.Str()
    create_time = fields.Float()
    arrival_time = fields.Float()
    is_private = fields.Bool()
    project_name = fields.Str()
    category = fields.Str()
    link = fields.Url(allow_none=True)
    seqno = fields.Int()

    @post_load
    def _remove_seqno(self, data, **kwargs):
        return remove_key(data, "seqno")


class Notices(Schema):
    notices = fields.Dict(fields.Int(), fields.Nested(Notice()))

    @pre_load
    def _a_normalise_none(self, data, **kwargs):
        return normalise_none_to_list(data, "notices")

    @pre_load
    def _b_flatten_data(self, data, **kwargs):
        return flatten_data(data, "notices", "notice")

    @pre_load
    def _c_create_dict_keys(self, data, **kwargs):
        return create_indexes(data, "notices", "seqno")
