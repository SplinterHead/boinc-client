from marshmallow import Schema, fields, post_load, pre_load

from boinc_client.models.helpers import (
    create_indexes,
    flatten_data,
    normalise_none_to_list,
    remove_key,
)


class Message(Schema):
    body = fields.Str(allow_none=True)
    pri = fields.Str()
    project = fields.Str(allow_none=True)
    seqno = fields.Int()
    time = fields.Int()

    @post_load
    def _a_remove_seqno(self, data, **kwargs):
        return remove_key(data, "seqno")


class Messages(Schema):
    messages = fields.Dict(fields.Int(), fields.Nested(Message()), data_key="msgs")

    @pre_load
    def _a_normalise_none(self, data, **kwargs):
        return normalise_none_to_list(data, "msgs")

    @pre_load
    def _b_flatten_data(self, data, **kwargs):
        return flatten_data(data, "msgs", "msg")

    @pre_load
    def _c_create_dict_keys(self, data, **kwargs):
        return create_indexes(data, "msgs", "seqno")
