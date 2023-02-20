from marshmallow import Schema, fields, post_load, pre_load


class MessageContent(Schema):
    project = fields.Str(allow_none=True)
    pri = fields.Str()
    body = fields.Str()
    time = fields.Int()
    seqno = fields.Int()

    @post_load
    def _remove_seqno(self, data, **kwargs):
        del data["seqno"]
        return data


class Messages(Schema):
    messages = fields.Dict(
        fields.Int(), fields.Nested(MessageContent()), data_key="msgs"
    )

    @pre_load
    def _convert_none_to_empty_dict(self, data, **kwargs):
        data["msgs"] = {} if not data["msgs"] else data["msgs"]["msg"]
        return data

    @pre_load
    def _create_dict_keys(self, data, **kwargs):
        data["msgs"] = {m["seqno"]: m for m in data["msgs"]}
        return data
