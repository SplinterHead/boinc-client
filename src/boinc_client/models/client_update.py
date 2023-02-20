from marshmallow import Schema, fields


class Update(Schema):
    newer_version = fields.Str(allow_none=True)
    download_url = fields.Url()


class ClientUpdate(Schema):
    update = fields.Nested(Update())
