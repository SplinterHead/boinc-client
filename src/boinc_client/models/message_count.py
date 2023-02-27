from marshmallow import Schema, fields


class MessageCount(Schema):
    message_count = fields.Int(data_key="seqno")
